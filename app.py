import os 
from apikey import apikey
import streamlit as st # type: ignore
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequantialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper

os.environ["OPENAI_API_KEY"] = apikey

# App framework
st.title("🦜🔗 Jaehee's learning GPT")
prompt = st.text_input("Plug in your prompt here:")

# Prompt templates
concept_template = PromptTemplate(
    input_variables=["concept"],
    template='write me an explanation paragraph about {concept}',
)

question_template = PromptTemplate(
    input_variables=["concept", "wikipedia_research"],
    template='write me a list of FAQ and answers about {concept} while leveraging this wikipedia research: {wikipedia_research}',
)

# Memory
concept_memory = ConversationBufferMemory(input_key='concept', memory_key='chat_history')
question_memory = ConversationBufferMemory(input_key='question', memory_key='chat_history')



# LLMs

llm = OpenAI(temperature=0.9)
concept_chain = LLMChain(llm=llm, prompt=concept_template, verbose=True, output_key="concept",
                         memory=concept_memory)

question_chain = LLMChain(llm=llm, prompt=question_template, verbose=True, output_key="question", memory=question_memory)
#sequential_chain = SequantialChain(chains=[concept_chain, question_chain],input_variables=['topic'],
#output_variables=['concept', 'question'], verbose=True)

wiki = WikipediaAPIWrapper()

# Show generated text on the screen if there's a prompt
if prompt:
    concept = concept_chain.run(prompt)
    wiki_research = wiki.run(prompt)
    question = question_chain.run(concept=concept, wikipedia_research=wiki_research)
    
    st.write(concept)
    st.write(question)

    with st.expander("Concept History"):
        st.info(concept_memory.buffer)
    
    with st.expander("Question History"):
        st.info(question_memory.buffer)

    with st.expander("Wikipedia Research"):
        st.info(wiki_research)