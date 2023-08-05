"""File generated by TLObjects' generator. All changes will be ERASED"""
from ...tl.tlobject import TLObject
from ...tl.tlobject import TLRequest
from typing import Optional, List, Union, TYPE_CHECKING
import os
import struct
from datetime import datetime
if TYPE_CHECKING:
    from ...tl.types import TypeCodeSettings, TypeEmailVerification, TypeInputCheckPasswordSRP
    from ...tl.types.account import TypePasswordInputSettings



class AcceptLoginTokenRequest(TLRequest):
    CONSTRUCTOR_ID = 0xe894ad4d
    SUBCLASS_OF_ID = 0xc913c01a

    def __init__(self, token: bytes):
        """
        :returns Authorization: Instance of Authorization.
        """
        self.token = token

    def to_dict(self):
        return {
            '_': 'AcceptLoginTokenRequest',
            'token': self.token
        }

    def _bytes(self):
        return b''.join((
            b'M\xad\x94\xe8',
            self.serialize_bytes(self.token),
        ))

    @classmethod
    def from_reader(cls, reader):
        _token = reader.tgread_bytes()
        return cls(token=_token)


class BindTempAuthKeyRequest(TLRequest):
    CONSTRUCTOR_ID = 0xcdd42a05
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, perm_auth_key_id: int, nonce: int, expires_at: Optional[datetime], encrypted_message: bytes):
        """
        :returns Bool: This type has no constructors.
        """
        self.perm_auth_key_id = perm_auth_key_id
        self.nonce = nonce
        self.expires_at = expires_at
        self.encrypted_message = encrypted_message

    def to_dict(self):
        return {
            '_': 'BindTempAuthKeyRequest',
            'perm_auth_key_id': self.perm_auth_key_id,
            'nonce': self.nonce,
            'expires_at': self.expires_at,
            'encrypted_message': self.encrypted_message
        }

    def _bytes(self):
        return b''.join((
            b'\x05*\xd4\xcd',
            struct.pack('<q', self.perm_auth_key_id),
            struct.pack('<q', self.nonce),
            self.serialize_datetime(self.expires_at),
            self.serialize_bytes(self.encrypted_message),
        ))

    @classmethod
    def from_reader(cls, reader):
        _perm_auth_key_id = reader.read_long()
        _nonce = reader.read_long()
        _expires_at = reader.tgread_date()
        _encrypted_message = reader.tgread_bytes()
        return cls(perm_auth_key_id=_perm_auth_key_id, nonce=_nonce, expires_at=_expires_at, encrypted_message=_encrypted_message)


class CancelCodeRequest(TLRequest):
    CONSTRUCTOR_ID = 0x1f040578
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, phone_number: str, phone_code_hash: str):
        """
        :returns Bool: This type has no constructors.
        """
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash

    def to_dict(self):
        return {
            '_': 'CancelCodeRequest',
            'phone_number': self.phone_number,
            'phone_code_hash': self.phone_code_hash
        }

    def _bytes(self):
        return b''.join((
            b'x\x05\x04\x1f',
            self.serialize_bytes(self.phone_number),
            self.serialize_bytes(self.phone_code_hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _phone_number = reader.tgread_string()
        _phone_code_hash = reader.tgread_string()
        return cls(phone_number=_phone_number, phone_code_hash=_phone_code_hash)


class CheckPasswordRequest(TLRequest):
    CONSTRUCTOR_ID = 0xd18b4d16
    SUBCLASS_OF_ID = 0xb9e04e39

    def __init__(self, password: 'TypeInputCheckPasswordSRP'):
        """
        :returns auth.Authorization: Instance of either Authorization, AuthorizationSignUpRequired.
        """
        self.password = password

    def to_dict(self):
        return {
            '_': 'CheckPasswordRequest',
            'password': self.password.to_dict() if isinstance(self.password, TLObject) else self.password
        }

    def _bytes(self):
        return b''.join((
            b'\x16M\x8b\xd1',
            self.password._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _password = reader.tgread_object()
        return cls(password=_password)


class CheckRecoveryPasswordRequest(TLRequest):
    CONSTRUCTOR_ID = 0xd36bf79
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, code: str):
        """
        :returns Bool: This type has no constructors.
        """
        self.code = code

    def to_dict(self):
        return {
            '_': 'CheckRecoveryPasswordRequest',
            'code': self.code
        }

    def _bytes(self):
        return b''.join((
            b'y\xbf6\r',
            self.serialize_bytes(self.code),
        ))

    @classmethod
    def from_reader(cls, reader):
        _code = reader.tgread_string()
        return cls(code=_code)


class DropTempAuthKeysRequest(TLRequest):
    CONSTRUCTOR_ID = 0x8e48a188
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, except_auth_keys: List[int]):
        """
        :returns Bool: This type has no constructors.
        """
        self.except_auth_keys = except_auth_keys

    def to_dict(self):
        return {
            '_': 'DropTempAuthKeysRequest',
            'except_auth_keys': [] if self.except_auth_keys is None else self.except_auth_keys[:]
        }

    def _bytes(self):
        return b''.join((
            b'\x88\xa1H\x8e',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.except_auth_keys)),b''.join(struct.pack('<q', x) for x in self.except_auth_keys),
        ))

    @classmethod
    def from_reader(cls, reader):
        reader.read_int()
        _except_auth_keys = []
        for _ in range(reader.read_int()):
            _x = reader.read_long()
            _except_auth_keys.append(_x)

        return cls(except_auth_keys=_except_auth_keys)


class ExportAuthorizationRequest(TLRequest):
    CONSTRUCTOR_ID = 0xe5bfffcd
    SUBCLASS_OF_ID = 0x5fd1ec51

    def __init__(self, dc_id: int):
        """
        :returns auth.ExportedAuthorization: Instance of ExportedAuthorization.
        """
        self.dc_id = dc_id

    def to_dict(self):
        return {
            '_': 'ExportAuthorizationRequest',
            'dc_id': self.dc_id
        }

    def _bytes(self):
        return b''.join((
            b'\xcd\xff\xbf\xe5',
            struct.pack('<i', self.dc_id),
        ))

    @classmethod
    def from_reader(cls, reader):
        _dc_id = reader.read_int()
        return cls(dc_id=_dc_id)


class ExportLoginTokenRequest(TLRequest):
    CONSTRUCTOR_ID = 0xb7e085fe
    SUBCLASS_OF_ID = 0x6b55f636

    def __init__(self, api_id: int, api_hash: str, except_ids: List[int]):
        """
        :returns auth.LoginToken: Instance of either LoginToken, LoginTokenMigrateTo, LoginTokenSuccess.
        """
        self.api_id = api_id
        self.api_hash = api_hash
        self.except_ids = except_ids

    def to_dict(self):
        return {
            '_': 'ExportLoginTokenRequest',
            'api_id': self.api_id,
            'api_hash': self.api_hash,
            'except_ids': [] if self.except_ids is None else self.except_ids[:]
        }

    def _bytes(self):
        return b''.join((
            b'\xfe\x85\xe0\xb7',
            struct.pack('<i', self.api_id),
            self.serialize_bytes(self.api_hash),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.except_ids)),b''.join(struct.pack('<q', x) for x in self.except_ids),
        ))

    @classmethod
    def from_reader(cls, reader):
        _api_id = reader.read_int()
        _api_hash = reader.tgread_string()
        reader.read_int()
        _except_ids = []
        for _ in range(reader.read_int()):
            _x = reader.read_long()
            _except_ids.append(_x)

        return cls(api_id=_api_id, api_hash=_api_hash, except_ids=_except_ids)


class ImportAuthorizationRequest(TLRequest):
    CONSTRUCTOR_ID = 0xa57a7dad
    SUBCLASS_OF_ID = 0xb9e04e39

    # noinspection PyShadowingBuiltins
    def __init__(self, id: int, bytes: bytes):
        """
        :returns auth.Authorization: Instance of either Authorization, AuthorizationSignUpRequired.
        """
        self.id = id
        self.bytes = bytes

    def to_dict(self):
        return {
            '_': 'ImportAuthorizationRequest',
            'id': self.id,
            'bytes': self.bytes
        }

    def _bytes(self):
        return b''.join((
            b'\xad}z\xa5',
            struct.pack('<q', self.id),
            self.serialize_bytes(self.bytes),
        ))

    @classmethod
    def from_reader(cls, reader):
        _id = reader.read_long()
        _bytes = reader.tgread_bytes()
        return cls(id=_id, bytes=_bytes)


class ImportBotAuthorizationRequest(TLRequest):
    CONSTRUCTOR_ID = 0x67a3ff2c
    SUBCLASS_OF_ID = 0xb9e04e39

    def __init__(self, flags: int, api_id: int, api_hash: str, bot_auth_token: str):
        """
        :returns auth.Authorization: Instance of either Authorization, AuthorizationSignUpRequired.
        """
        self.flags = flags
        self.api_id = api_id
        self.api_hash = api_hash
        self.bot_auth_token = bot_auth_token

    def to_dict(self):
        return {
            '_': 'ImportBotAuthorizationRequest',
            'flags': self.flags,
            'api_id': self.api_id,
            'api_hash': self.api_hash,
            'bot_auth_token': self.bot_auth_token
        }

    def _bytes(self):
        return b''.join((
            b',\xff\xa3g',
            struct.pack('<i', self.flags),
            struct.pack('<i', self.api_id),
            self.serialize_bytes(self.api_hash),
            self.serialize_bytes(self.bot_auth_token),
        ))

    @classmethod
    def from_reader(cls, reader):
        _flags = reader.read_int()
        _api_id = reader.read_int()
        _api_hash = reader.tgread_string()
        _bot_auth_token = reader.tgread_string()
        return cls(flags=_flags, api_id=_api_id, api_hash=_api_hash, bot_auth_token=_bot_auth_token)


class ImportLoginTokenRequest(TLRequest):
    CONSTRUCTOR_ID = 0x95ac5ce4
    SUBCLASS_OF_ID = 0x6b55f636

    def __init__(self, token: bytes):
        """
        :returns auth.LoginToken: Instance of either LoginToken, LoginTokenMigrateTo, LoginTokenSuccess.
        """
        self.token = token

    def to_dict(self):
        return {
            '_': 'ImportLoginTokenRequest',
            'token': self.token
        }

    def _bytes(self):
        return b''.join((
            b'\xe4\\\xac\x95',
            self.serialize_bytes(self.token),
        ))

    @classmethod
    def from_reader(cls, reader):
        _token = reader.tgread_bytes()
        return cls(token=_token)


class ImportWebTokenAuthorizationRequest(TLRequest):
    CONSTRUCTOR_ID = 0x2db873a9
    SUBCLASS_OF_ID = 0xb9e04e39

    def __init__(self, api_id: int, api_hash: str, web_auth_token: str):
        """
        :returns auth.Authorization: Instance of either Authorization, AuthorizationSignUpRequired.
        """
        self.api_id = api_id
        self.api_hash = api_hash
        self.web_auth_token = web_auth_token

    def to_dict(self):
        return {
            '_': 'ImportWebTokenAuthorizationRequest',
            'api_id': self.api_id,
            'api_hash': self.api_hash,
            'web_auth_token': self.web_auth_token
        }

    def _bytes(self):
        return b''.join((
            b'\xa9s\xb8-',
            struct.pack('<i', self.api_id),
            self.serialize_bytes(self.api_hash),
            self.serialize_bytes(self.web_auth_token),
        ))

    @classmethod
    def from_reader(cls, reader):
        _api_id = reader.read_int()
        _api_hash = reader.tgread_string()
        _web_auth_token = reader.tgread_string()
        return cls(api_id=_api_id, api_hash=_api_hash, web_auth_token=_web_auth_token)


class LogOutRequest(TLRequest):
    CONSTRUCTOR_ID = 0x3e72ba19
    SUBCLASS_OF_ID = 0xa804315

    def to_dict(self):
        return {
            '_': 'LogOutRequest'
        }

    def _bytes(self):
        return b''.join((
            b'\x19\xbar>',
        ))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class RecoverPasswordRequest(TLRequest):
    CONSTRUCTOR_ID = 0x37096c70
    SUBCLASS_OF_ID = 0xb9e04e39

    def __init__(self, code: str, new_settings: Optional['TypePasswordInputSettings']=None):
        """
        :returns auth.Authorization: Instance of either Authorization, AuthorizationSignUpRequired.
        """
        self.code = code
        self.new_settings = new_settings

    def to_dict(self):
        return {
            '_': 'RecoverPasswordRequest',
            'code': self.code,
            'new_settings': self.new_settings.to_dict() if isinstance(self.new_settings, TLObject) else self.new_settings
        }

    def _bytes(self):
        return b''.join((
            b'pl\t7',
            struct.pack('<I', (0 if self.new_settings is None or self.new_settings is False else 1)),
            self.serialize_bytes(self.code),
            b'' if self.new_settings is None or self.new_settings is False else (self.new_settings._bytes()),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _code = reader.tgread_string()
        if flags & 1:
            _new_settings = reader.tgread_object()
        else:
            _new_settings = None
        return cls(code=_code, new_settings=_new_settings)


class RequestPasswordRecoveryRequest(TLRequest):
    CONSTRUCTOR_ID = 0xd897bc66
    SUBCLASS_OF_ID = 0xfa72d43a

    def to_dict(self):
        return {
            '_': 'RequestPasswordRecoveryRequest'
        }

    def _bytes(self):
        return b''.join((
            b'f\xbc\x97\xd8',
        ))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class ResendCodeRequest(TLRequest):
    CONSTRUCTOR_ID = 0x3ef1a9bf
    SUBCLASS_OF_ID = 0x6ce87081

    def __init__(self, phone_number: str, phone_code_hash: str):
        """
        :returns auth.SentCode: Instance of SentCode.
        """
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash

    def to_dict(self):
        return {
            '_': 'ResendCodeRequest',
            'phone_number': self.phone_number,
            'phone_code_hash': self.phone_code_hash
        }

    def _bytes(self):
        return b''.join((
            b'\xbf\xa9\xf1>',
            self.serialize_bytes(self.phone_number),
            self.serialize_bytes(self.phone_code_hash),
        ))

    @classmethod
    def from_reader(cls, reader):
        _phone_number = reader.tgread_string()
        _phone_code_hash = reader.tgread_string()
        return cls(phone_number=_phone_number, phone_code_hash=_phone_code_hash)


class ResetAuthorizationsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x9fab0d1a
    SUBCLASS_OF_ID = 0xf5b399ac

    def to_dict(self):
        return {
            '_': 'ResetAuthorizationsRequest'
        }

    def _bytes(self):
        return b''.join((
            b'\x1a\r\xab\x9f',
        ))

    @classmethod
    def from_reader(cls, reader):
        return cls()


class SendCodeRequest(TLRequest):
    CONSTRUCTOR_ID = 0xa677244f
    SUBCLASS_OF_ID = 0x6ce87081

    def __init__(self, phone_number: str, api_id: int, api_hash: str, settings: 'TypeCodeSettings'):
        """
        :returns auth.SentCode: Instance of SentCode.
        """
        self.phone_number = phone_number
        self.api_id = api_id
        self.api_hash = api_hash
        self.settings = settings

    def to_dict(self):
        return {
            '_': 'SendCodeRequest',
            'phone_number': self.phone_number,
            'api_id': self.api_id,
            'api_hash': self.api_hash,
            'settings': self.settings.to_dict() if isinstance(self.settings, TLObject) else self.settings
        }

    def _bytes(self):
        return b''.join((
            b'O$w\xa6',
            self.serialize_bytes(self.phone_number),
            struct.pack('<i', self.api_id),
            self.serialize_bytes(self.api_hash),
            self.settings._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _phone_number = reader.tgread_string()
        _api_id = reader.read_int()
        _api_hash = reader.tgread_string()
        _settings = reader.tgread_object()
        return cls(phone_number=_phone_number, api_id=_api_id, api_hash=_api_hash, settings=_settings)


class SignInRequest(TLRequest):
    CONSTRUCTOR_ID = 0x8d52a951
    SUBCLASS_OF_ID = 0xb9e04e39

    def __init__(self, phone_number: str, phone_code_hash: str, phone_code: Optional[str]=None, email_verification: Optional['TypeEmailVerification']=None):
        """
        :returns auth.Authorization: Instance of either Authorization, AuthorizationSignUpRequired.
        """
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
        self.phone_code = phone_code
        self.email_verification = email_verification

    def to_dict(self):
        return {
            '_': 'SignInRequest',
            'phone_number': self.phone_number,
            'phone_code_hash': self.phone_code_hash,
            'phone_code': self.phone_code,
            'email_verification': self.email_verification.to_dict() if isinstance(self.email_verification, TLObject) else self.email_verification
        }

    def _bytes(self):
        return b''.join((
            b'Q\xa9R\x8d',
            struct.pack('<I', (0 if self.phone_code is None or self.phone_code is False else 1) | (0 if self.email_verification is None or self.email_verification is False else 2)),
            self.serialize_bytes(self.phone_number),
            self.serialize_bytes(self.phone_code_hash),
            b'' if self.phone_code is None or self.phone_code is False else (self.serialize_bytes(self.phone_code)),
            b'' if self.email_verification is None or self.email_verification is False else (self.email_verification._bytes()),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _phone_number = reader.tgread_string()
        _phone_code_hash = reader.tgread_string()
        if flags & 1:
            _phone_code = reader.tgread_string()
        else:
            _phone_code = None
        if flags & 2:
            _email_verification = reader.tgread_object()
        else:
            _email_verification = None
        return cls(phone_number=_phone_number, phone_code_hash=_phone_code_hash, phone_code=_phone_code, email_verification=_email_verification)


class SignUpRequest(TLRequest):
    CONSTRUCTOR_ID = 0x80eee427
    SUBCLASS_OF_ID = 0xb9e04e39

    def __init__(self, phone_number: str, phone_code_hash: str, first_name: str, last_name: str):
        """
        :returns auth.Authorization: Instance of either Authorization, AuthorizationSignUpRequired.
        """
        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self):
        return {
            '_': 'SignUpRequest',
            'phone_number': self.phone_number,
            'phone_code_hash': self.phone_code_hash,
            'first_name': self.first_name,
            'last_name': self.last_name
        }

    def _bytes(self):
        return b''.join((
            b"'\xe4\xee\x80",
            self.serialize_bytes(self.phone_number),
            self.serialize_bytes(self.phone_code_hash),
            self.serialize_bytes(self.first_name),
            self.serialize_bytes(self.last_name),
        ))

    @classmethod
    def from_reader(cls, reader):
        _phone_number = reader.tgread_string()
        _phone_code_hash = reader.tgread_string()
        _first_name = reader.tgread_string()
        _last_name = reader.tgread_string()
        return cls(phone_number=_phone_number, phone_code_hash=_phone_code_hash, first_name=_first_name, last_name=_last_name)

