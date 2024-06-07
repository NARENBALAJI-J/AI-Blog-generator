
import streamlit as st
import google.generativeai as genai
from apikey import google_gemini_api_key,openai_api_key
#from openai import OpenAI
#client =OpenAI(api_key=openai_api_key)
genai.configure(api_key="AIzaSyDOv-fHcjU64JNB8TymKC_3ryA3MDoFBec")

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]
#setting up our model 
model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  safety_settings=safety_settings,
  generation_config=generation_config,
)


#set app to wide mode
st.set_page_config(layout="wide")
#title of our app
st.title("BlogAI: Your AI Writing Companion")
#create a subheader
st.subheader("Now you can craft perfect blogs with the help of AI-BlogCraft is your new Ai Blog Companion")

#sidebar for user input
with st.sidebar:
    st.title("input your Blog Detail")
    st.subheader("enter details of the blog you want to generate")

    #blog title
    blog_title=st.text_input("Blog Title")

    #keywords input
    keywords=st.text_area("Keywords(comma-separated)")

    #number of words
    num_words=st.slider("number of words",min_value=100,max_value=1000,step=100)
  
    #number of images
    num_images = st.number_input("Number of images",min_value=1,max_value=10,step=1)

    prompt_parts =[
        f"Genarate a comprehensive,engaging blog post relevant to the given title \"{blog_title}\" and keywords \"{keywords} \".Make sure to incorporate these keywords in the blog post.The blog should be approximately {num_words} words in length,suitable for an online auidence.Ensure the content is original,informative,and maintains a consistent tone throughout",
    ]
    

    #submit button
    submit_button=st.button("Generate Blog")

if submit_button:
    #st.image("/Users/aswathkumark/Desktop/project/images/NISSAN/blog-2.jpg")
    response = model.generate_content(prompt_parts)

   # image_response=client.images.generate(
    #model="dall-e-3",
    #prompt="a white siamese cat",
    ##quality="standard",
    #n=1,

   # )
    #image_url=image_response.date[0].url


    #st.image(image_url,caption="Generated Image")
    st.title("YOUR BLOG POST:")

    st.write(response.text)