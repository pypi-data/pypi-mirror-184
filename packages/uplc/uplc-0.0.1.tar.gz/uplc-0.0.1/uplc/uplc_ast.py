import logging
from dataclasses import dataclass
from functools import partial
from enum import Enum, auto
import hashlib

_LOGGER = logging.getLogger(__name__)


class ConstantType(Enum):
    integer = auto()
    bytestring = auto()
    string = auto()
    unit = auto()
    bool = auto()


ConstantEvalMap = {
    ConstantType.integer: int,
    ConstantType.bytestring: lambda x: bytes.fromhex(x[1:]),
    ConstantType.string: lambda x: str(x).encode("utf8"),
    ConstantType.unit: lambda _: (),
    ConstantType.bool: bool,
}


# As found in https://plutonomicon.github.io/plutonomicon/builtin-functions
class BuiltInFun(Enum):
    AddInteger = auto()
    SubtractInteger = auto()
    MultiplyInteger = auto()
    DivideInteger = auto()
    QuotientInteger = auto()
    RemainderInteger = auto()
    ModInteger = auto()
    EqualsInteger = auto()
    LessThanInteger = auto()
    LessThanEqualsInteger = auto()
    AppendByteString = auto()
    ConsByteString = auto()
    SliceByteString = auto()
    LengthOfByteString = auto()
    IndexByteString = auto()
    EqualsByteString = auto()
    LessThanByteString = auto()
    LessThanEqualsByteString = auto()
    Sha2_256 = auto()
    Sha3_256 = auto()
    Blake2b_256 = auto()
    VerifySignature = auto()
    AppendString = auto()
    EqualsString = auto()
    EncodeUtf8 = auto()
    DecodeUtf8 = auto()
    IfThenElse = auto()
    ChooseUnit = auto()
    Trace = auto()
    FstPair = auto()
    SndPair = auto()
    ChooseList = auto()
    MkCons = auto()
    HeadList = auto()
    TailList = auto()
    NullList = auto()
    ChooseData = auto()
    ConstrData = auto()
    MapData = auto()
    ListData = auto()
    IData = auto()
    BData = auto()
    UnConstrData = auto()
    UnMapData = auto()
    UnListData = auto()
    UnIData = auto()
    EqualsData = auto()
    MkPairData = auto()
    MkNilData = auto()
    MkNilPairData = auto()


BuiltInFunEvalMap = {
    BuiltInFun.AddInteger: lambda x, y: x + y,
    BuiltInFun.SubtractInteger: lambda x, y: x - y,
    BuiltInFun.MultiplyInteger: lambda x, y: x * y,
    # TODO difference with negative values?
    BuiltInFun.DivideInteger: lambda x, y: x // y,
    BuiltInFun.QuotientInteger: lambda x, y: x // y,
    # TODO difference with negative values?
    BuiltInFun.RemainderInteger: lambda x, y: x % y,
    BuiltInFun.ModInteger: lambda x, y: x % y,
    BuiltInFun.EqualsInteger: lambda x, y: x == y,
    BuiltInFun.LessThanInteger: lambda x, y: x < y,
    BuiltInFun.LessThanEqualsInteger: lambda x, y: x <= y,
    BuiltInFun.AppendByteString: lambda x, y: x + y,
    BuiltInFun.ConsByteString: lambda x, y: bytes([x]) + y,
    BuiltInFun.SliceByteString: lambda x, y, z: z[x : y + 1],
    BuiltInFun.LengthOfByteString: lambda x: len(x),
    BuiltInFun.IndexByteString: lambda x, y: x[y],
    BuiltInFun.EqualsByteString: lambda x, y: x == y,
    BuiltInFun.LessThanByteString: lambda x, y: x < y,
    BuiltInFun.LessThanEqualsByteString: lambda x, y: x <= y,
    BuiltInFun.Sha2_256: lambda x: hashlib.sha256(x).digest(),
    BuiltInFun.Sha3_256: lambda x: hashlib.sha3_256(x).digest(),
    BuiltInFun.Blake2b_256: lambda x: hashlib.blake2b(x).digest(),
    # TODO how to emulate this?
    BuiltInFun.VerifySignature: lambda pk, m, s: True,
    BuiltInFun.AppendString: lambda x, y: x + y,
    BuiltInFun.EqualsString: lambda x, y: x == y,
    BuiltInFun.EncodeUtf8: lambda x: x.encode("utf8"),
    BuiltInFun.DecodeUtf8: lambda x: x.decode("utf8"),
    BuiltInFun.IfThenElse: lambda x, y, z: y if x else z,
    BuiltInFun.ChooseUnit: lambda x, y: y,
    BuiltInFun.Trace: lambda x, y: print(x) or y,
    BuiltInFun.FstPair: lambda x: lambda _: lambda _: x[0],
    BuiltInFun.SndPair: lambda x: lambda _: lambda _: x[1],
    # TODO proper implementation
    BuiltInFun.UnIData: lambda x: int(x),
    BuiltInFun.UnConstrData: lambda x: (0, x.__dict__.keys()),
    BuiltInFun.NullList: lambda x: lambda _: x == [],
    BuiltInFun.HeadList: lambda x: lambda _: x[0],
    BuiltInFun.TailList: lambda x: lambda _: x[1:],
}


class AST:
    def eval(self, state: dict):
        raise NotImplementedError()

    def dumps(self) -> str:
        raise NotImplementedError()


@dataclass
class Program(AST):
    version: str
    term: AST

    def eval(self, state):
        return self.term.eval(state)

    def dumps(self) -> str:
        return f"(program {self.version} {self.term.dumps()})"


@dataclass
class Variable(AST):
    name: str

    def eval(self, state):
        try:
            return state[self.name]
        except KeyError as e:
            _LOGGER.error(
                f"Access to uninitialized variable {self.name} in {self.dumps()}"
            )
            raise e

    def dumps(self) -> str:
        return self.name


@dataclass
class Constant(AST):
    type: ConstantType
    value: str

    def eval(self, state):
        return self.type.value(self.value)

    def dumps(self) -> str:
        return f"(con {self.type.name} {self.value})"


@dataclass
class Lambda(AST):
    var_name: str
    term: AST

    def eval(self, state):
        def f(x):
            return self.term.eval(state | {self.var_name: x})

        return partial(f)

    def dumps(self) -> str:
        return f"(lam {self.var_name} {self.term.dumps()})"


@dataclass
class Delay(AST):
    term: AST

    def eval(self, state):
        def f():
            return self.term.eval(state)

        return f

    def dumps(self) -> str:
        return f"(delay {self.term.dumps()})"


@dataclass
class Force(AST):
    term: AST

    def eval(self, state):
        try:
            return self.term.eval(state)()
        except TypeError as e:
            _LOGGER.error(
                f"Trying to force an uncallable object, probably not delayed? in {self.dumps()}"
            )
            raise e

    def dumps(self) -> str:
        return f"(force {self.term.dumps()})"


@dataclass
class BuiltIn(AST):
    builtin: BuiltInFun

    def eval(self, state):
        return partial(BuiltInFunEvalMap[self.builtin])

    def dumps(self) -> str:
        return f"(builtin {self.builtin.name[0].lower()}{self.builtin.name[1:]})"


@dataclass
class Error(AST):
    def eval(self, state):
        raise RuntimeError(f"Execution called {self.dumps()}")

    def dumps(self) -> str:
        return f"(error)"


@dataclass
class Apply(AST):
    f: AST
    x: AST

    def eval(self, state):
        f = self.f.eval(state)
        x = self.x.eval(state)
        try:
            res = partial(f, x)
            # If this function has as many arguments bound as it takes, reduce i.e. call
            if len(f.args) == f.func.__code__.co_argcount:
                res = f()
            return res
        except AttributeError as e:
            _LOGGER.warning(f"Tried to apply value to non-function in {self.dumps()}")
            raise e

    def dumps(self) -> str:
        return f"[{self.f.dumps()} {self.x.dumps()}]"
