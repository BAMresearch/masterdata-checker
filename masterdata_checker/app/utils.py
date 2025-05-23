import uuid

from cryptography.fernet import Fernet, InvalidToken
from django.conf import settings
from django.core.cache import cache
from pybis import Openbis

# Instantiate the Fernet class with the secret key
cipher_suite = Fernet(settings.SECRET_ENCRYPTION_KEY)


# Encrypt the password
def encrypt_password(plain_text_password):
    encrypted_password = cipher_suite.encrypt(plain_text_password.encode("utf-8"))
    return encrypted_password.decode("utf-8")  # Return as a string


def decrypt_password(encrypted_password):
    try:
        # Remove the manual padding correction, Fernet handles it automatically
        decrypted_password = cipher_suite.decrypt(encrypted_password.encode("utf-8"))
        return decrypted_password.decode("utf-8")
    except InvalidToken as e:
        print(f"Decryption failed: {str(e)}")
        raise InvalidToken("Decryption failed due to an invalid token.")
    except Exception as e:
        print(f"Decryption error: {str(e)}")
        raise e


def get_openbis_from_cache(request):
    session_id = request.session.get("openbis_session_id")
    if session_id:
        o = cache.get(session_id)
        if o:
            return o

    # If cache expired or object missing, force relogin:
    username = request.session.get("openbis_username")
    encrypted_password = request.session.get("openbis_password")

    if username and encrypted_password:
        password = decrypt_password(encrypted_password)
        o = Openbis(settings.OPENBIS_URL)
        o.login(username, password, save_token=True)

        # Cache again
        session_id = str(uuid.uuid4())
        request.session["openbis_session_id"] = session_id
        cache.set(session_id, o, timeout=60 * 60)

        return o

    return None
