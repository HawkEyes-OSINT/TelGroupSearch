from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError
from in_out import getconfig, get_keywords
import asyncio


async def main():

    # create client session
    print('[+] Creating Telegram client session')
    config = getconfig()
    client = TelegramClient('session', config['api_id'], config['api_hash'])
    await client.start(config['phone'])
    if not client.is_user_authorized():
        client.send_code_request(config['phone'])
        try:
            client.sign_in(config['phone'], input('Enter the code: '))
        except SessionPasswordNeededError: # 2FA auth
            client.sign_in(phone=config['phone'], password=input('Enter 2FA password: '))
        except Exception as e:
            print('[-] ' + e)
            exit(0)
    print('[+] Client session created')

    # get keyword
    keywords = get_keywords()


if __name__ == "__main__":
    asyncio.run(main())
