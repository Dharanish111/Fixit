import streamlit as st
st.header("Fixit✨ (The AI Chatbot):")
"""In today's fast-paced and digital-driven world, efficient communication forms the backbone of successful businesses. One such technology that has reshaped the landscape of digital communication is the 'Chatbot'—an AI-powered program designed to interact with humans in their natural languages. These dialogues can take place on any platform, such as messaging apps, websites, mobile apps, or even over the phone.
"""

image_1 = st.image("/home/dharanish/Fixit/Fixit/pics/fixit1.jpg")

st.markdown("I created a chatbot named Fixit. It is a multi-API chatbot and can respond in all official languages of India. Additionally, I have set a reminder feature which is useful for maintaining punctuality. The Fixit chatbot also supports file inputs such as .txt, .pdf, and .docx, which can be provided by the user.")

image_2 = st.image("/home/dharanish/Fixit/Fixit/pics/fixit2.jpg")

st.subheader(":orange[API SELECTION:]")

image_3 = st.image("/home/dharanish/Fixit/Fixit/pics/api.jpg")

st.markdown("An API (application programming interface) is a set of instructions that allows software to communicate with other software.They are a way for different programs to share data and functionality. I have placed radio buttons to switch between two prefered APIs (Openai & Gemini).")
   
multi =   """  • User can select any API and can get response from selected AI.
   
• Once any API is selected,it shows selected API below the radio buttons.
"""
st.markdown(multi)
 
st.subheader(":orange[FILE UPLOADER:]")

image_4 = st.image("/home/dharanish/Fixit/Fixit/pics/fileuploader.jpg")

"""
The image is a screenshot of a file upload screen.						
The text at the bottom instructs users to drag and drop files or browse files.It also specifies that there is a maximum file size of 200MB and that the supported file types are TXT,PDF and DOCX.

    • This image shows a user-friendly file upload screen with clear instructions.
    • Users can drag and drop files or browse their computer for files to upload.
    • The screen specifies that the maximum file size is 200MB and that only TXT,PDF and DOCX files are supported.
    """

st.subheader(":orange[Reminder:]")

image_5 = st.image("/home/dharanish/Fixit/Fixit/pics/reminder.jpg")

st.markdown("The image is a reminder screen with a reminder message, reminder time, and set reminder button. Here are some details about the image:")

multi = """User can set a reminder by entering a message and then selecting a time.

Once the reminder is set, it will be listed in the "All Reminders" section.
"""

"""
**Text:**

    • Set a Reminder
    • Reminder Message
    • Reminder (blank space for message)
    • Time (shows 06:11 AM)
    • Set Reminder
    • All Reminders
"""


"""
**Layout:**

    • The top section has a text header "Set a Reminder".
    • Below the header, there are two text fields. One for the reminder message and another for the reminder time.
    • A button labeled "Set Reminder" is located below the time field.
    • Below the button is a section titled "All Reminders".
"""
st.markdown(multi)

st.subheader(":orange[LANGUAGES SELECTION:]")

image_6 = st.image("/home/dharanish/Fixit/Fixit/pics/languages.jpg")

st.markdown("The  screenshot of a select language screen.I have used selectbox to choose preferred language from list.")
 
multi = """It supports multiple languages.The user can select their preferred language from the list.

It has all Indian Languages.
"""

"""
**Text:**

    ◦ Select a language
    ◦ English (selected)
    ◦ English
    ◦ Telugu
    ◦ Hindi
    ◦ Tamil
    ◦ Marathi
    ◦ Sanskrit
    ◦ Bengali
"""

"""       
**Layout:**

    ◦ The screen title is “Select a language”.
    ◦ Below the title, there is a list of eight languages. English is currently selected.
"""

st.subheader(":orange[CHAT HISTORY:]")

image_7 = st.image("/home/dharanish/Fixit/Fixit/pics/chathistory.jpg")

"""

The above image is a screenshot of a chat history between a user and an assistant named Fixit. Also I placed history text box which stores the responsed data.

      Text:
        ◦ Chat History
        ◦ You: Hello
        ◦ Fixit: Hello! How can I assist you today?
        ◦ You: Hello
        ◦ Fixit: హలో
      Layout:
        ◦ The chat history is displayed in a chat window.
        ◦ The user’s messages are displayed on the left side of the chat window and Fixit’s messages are displayed on the right side.
        ◦ The most recent message is at the bottom of the chat window.
This is a basic chat interface where a user can interact with a virtual assistant named Fixit. Fixit offers to assist the user.
"""
