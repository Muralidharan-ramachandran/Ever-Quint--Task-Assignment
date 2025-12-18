from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from config import LLM_MODEL


llm = ChatOpenAI(model=LLM_MODEL)


prompt = PromptTemplate(
    input_variables=["context", "length"],
    template="""
Summarize the following text in approximately {length} words.

{context}
"""
)


def summarize(documents, length):
    context = "\n\n".join(documents)
    return llm.predict(prompt.format(context=context, length=length))