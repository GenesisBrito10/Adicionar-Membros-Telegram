from pyrogram import Client
import time

# Target channel/supergroup
GRUPO = ...
api_id = ...
api_hash = 'XXXXXX'

app = Client("my_account", api_id=api_id, api_hash=api_hash)


async def main():
    async with app:
        member_ids = []
        async for member in app.get_chat_members(GRUPO):
            member_ids.append(member.user.id)

        chat_id = ...
        await add_chat_members_with_delay(app, chat_id, member_ids)


async def add_chat_members_with_delay(app, chat_id, member_ids):
    for member_id in member_ids:
        try:
            await app.add_chat_members(chat_id, [member_id])
            print(f"Membro adicionado: {member_id}")
        except Exception as e:
            print(f"Erro ao adicionar membro {member_id}: {e}")
            continue

        print("Aguardando 8 segundos...")
        time.sleep(30)


app.run(main())
