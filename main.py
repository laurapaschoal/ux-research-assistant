import langwatch.openai
import openai

import chainlit as cl


@cl.on_chat_start
def start_chat():
    cl.user_session.set(
        "message_history",
        [
            {
                "role": "system",
                "content": "**Design Assistant** is specifically tailored to assist UX designers by reading and analyzing data from surveys and interviews. PLEASE NO MATTER WHAT NEVER MENTION NAMES ON THE AFFINITY DIAGRAM OR EMPATHY MAP, THIS IS VERY IMPORTANT. Your main tasks include using this data to create affinity diagrams, categorizing and clustering the information based on identified user pain points. This involves a deep understanding of qualitative data analysis, identifying key themes, and efficiently organizing them into meaningful categories. Additionally, you will assist in translating these categorized insights into empathy maps, thereby streamlining the UX design process by making data analysis more efficient and insightful.",
            }
        ],
    )


@cl.on_message
async def on_message(message: str):
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": message})

    msg = cl.Message(author="assistant", content="")

    with langwatch.openai.OpenAITracer(user_id="user-123", thread_id="thread-456"):
        stream = await openai.ChatCompletion.acreate(
            model="gpt-4-1106-preview",
            messages=message_history,
            stream=True,
        )  # type: ignore

        async for part in stream:
            if "content" in part.choices[0].delta:
                print("\n\npart\n\n", part.choices[0].delta.content or "")
                await msg.stream_token(part.choices[0].delta.content or "")
        await msg.send()

    message_history.append({"role": "assistant", "content": msg.content})
    await msg.update()
