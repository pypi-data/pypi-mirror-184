# ProofUtils ✨

`📝 Information:`

An easy-to-use package used for generating **fake nitro gifting proof** for Discord. You are able to create bots with this package and use them for fake nitro servers on Discord as a "**Discord Nitro Proof Bot**". 🤖

It uses **[HTML2Image](https://htmlcsstoimage.com/)** to return an image of your nitro gifting proof and **[this](https://github.com/itschasa/Discord-Scraped)** repository to fetch random avatars.

`📥 Installation:`

You are able to **install** the package directly through **PIP** using the following command:

```
pip install proofutils
```

*Then simply import the package and use it as you wish.*

`💻 Usage:`

The **following** code is an example of how you could use the package using **[discord.py](https://github.com/Rapptz/discord.py)**.

```py
async def proof(interaction: discord.Interaction, type: app_commands.Choice[int], receiver_username: str, question: str, response: str):
  await interaction.response.defer(thinking=True)
  proof = ProofUtils(sender_username=interaction.user.name, sender_avatar=interaction.user.avatar.url, receiver_username=receiver_username, messages=[question, response], nitro_type=type.value).generate()
  await interaction.channel.send(content=f"Your Proof: <@{interaction.user.id}>", files=[discord.File(proof, "proof.png")])
```

`👨‍💻 Example:`

Here's a simple example of using ProofUtils.

```py
from proofutils import ProofUtils

generator = ProofUtils(sender_username="Derick", sender_avatar="https://discord.com/assets/7c8f476123d28d103efe381543274c25.png", receiver_username="Hey", messages=["Can I have my nitro?\nPlease!", "Thanks!"])
generator.generate() # Returns an image of your proof in bytes (io.BytesIO)
```

`📜 Parameters:`

| Parameter | Description |
| --- | --- |
| `sender_username` | The username of the user "gifting" nitro. |
| `sender_avatar` | A URL to the user's avatar who is sending the nitro. |
| `receiver_username` | The username of the user who will be asking for the nitro. |
| `messages` | A **[list](https://www.w3schools.com/python/python_lists.asp)** containing 2 messages (1: question, 2: response to nitro). Use **\n** to create a new line. |
| `nitro_type` | An integer (1-3) which will represent the nitro you are giving. (1. Regular Nitro, 2. Classic Nitro & 3. Basic Nitro.) |
| `html_client` | **Optional:** Class of the HTML2Image client. |

All of the functions are documented in detail.

`🎨 Images:`

![image](https://user-images.githubusercontent.com/121643953/211116304-510cb1fb-68ba-4c16-8203-e25f8c01be59.png)

## Contributing
All contributions are appreciated. To contribute to the package, open a **[pull request](https://github.com/ercenterprises/ProofUtils/pulls)**. 🙏

## Request Features
Open an **[issue](https://github.com/ercenterprises/ProofUtils/labels)** and use the "feature request" tag to request new features! 💖
