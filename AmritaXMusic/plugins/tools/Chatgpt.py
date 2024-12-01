from TheApi import api
from pyrogram import Client, filters
from pyrogram.enums import ChatAction
from config import BANNED_USERS  # Assuming you have banned users defined in your config

# Set your OpenAI API key
openai.api_key = 'ckey_01cdf01902dc8a2773eb58b2cac8'  # Replace with your actual OpenAI API key

# Function to interact with OpenAI's API
def chatgpt(prompt):
    try:
        # Make a request to OpenAI GPT-3.5 or GPT-4 (change engine if needed)
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",  # Or "gpt-4" if you want to use GPT-4
            prompt=prompt,
            max_tokens=150,           # Limit the response to 150 tokens
            temperature=0.7,          # Controls the randomness of the response
            top_p=1.0,                # Controls diversity via nucleus sampling
            frequency_penalty=0.0,    # Penalizes repeated phrases
            presence_penalty=0.0      # Penalizes new topics or unexpected responses
        )

        # Return the text response from the model
        return response.choices[0].text.strip()

    except Exception as e:
        # If there's an error, return a message indicating the error
        return f"Error: {str(e)}"


# Initialize the bot application
app = Client("my_bot")

# Command handler for language detection and chatbot-like responses
@app.on_message(filters.command(["detect", "aidetect", "asklang"]) & ~BANNED_USERS)
async def chatgpt_chat_lang(bot, message):
    if len(message.command) < 2 and not message.reply_to_message:
        await message.reply_text("**Please provide some text after the command or reply to a message**")
        return

    # Check if the message is a reply
    if message.reply_to_message and message.reply_to_message.text:
        user_text = message.reply_to_message.text
    else:
        user_text = " ".join(message.command[1:])

    # Prepare the prompt for ChatGPT
    user_input = f"""
    Sentences :- {user_text}
    Ye sentence kon sa language me hai mujhe bas ush sentences ka lang name aur lang code, sath me ush sentence ka chatbot jaisa chhota se chhota reply do jyada bada reply mat dena maximum 1 sentence ka hona chahiye reply aur agar chhota se chhota reply me bhi kam ho ja rha hai to chhota hi reply do aur jis lang me sentence hai usi lang me likh ke do, agar sentence me sirf emoji hoga to tum bhi bas emoji dena aur ish format me likh ke do :- 

    Lang : -
    Code :-
    Reply :- 

    Bas lang name aur lang code aur reply likh ke do uske alava kuch nhi
    """

    # Send typing action and get the response from the API
    await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    results = chatgpt(user_input)  # Call the chatgpt function
    await message.reply_text(results)


# Main ChatGPT functionality for user queries
@app.on_message(filters.command(["chatgpt", "ai", "ask"]) & ~BANNED_USERS)
async def chatgpt_chat(bot, message):
    if len(message.command) < 2 and not message.reply_to_message:
        await message.reply_text("**Example usage**:\n\n`/ai Write simple website code using HTML, CSS, JS`")
        return

    # Check if the message is a reply
    if message.reply_to_message and message.reply_to_message.text:
        user_input = message.reply_to_message.text
    else:
        user_input = " ".join(message.command[1:])

    # Send typing action and get the response from the API
    await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    results = chatgpt(user_input)  # Call the chatgpt function
    await message.reply_text(results)


# Module Metadata
__MODULE__ = "CʜᴀᴛGᴘᴛ"
__HELP__ = """
/advice - Get random advice from the bot
/ai [query] - Ask ChatGPT anything you want
/gemini [query] - Ask Google's Gemini AI anything you want
/bard [query] - Ask Google's Bard AI anything you want
"""

# Start the bot
if __name__ == "__main__":
    app.run()
  
