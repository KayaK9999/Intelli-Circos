from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from chain import intelliCircos_model, OutputType, ChatInput
from langserve import add_routes
import logging
from explain import similarity_search
from typing import List

logging.basicConfig(level=logging.DEBUG)


app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

origins = [
    "*",
]

add_routes(
    app,
    intelliCircos_model.with_types(output_type=OutputType),
    path="/recommend",
)

# 使用中间键配置跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/search", response_model=List[str])
async def search(input: str):
    # 调用 similarity_search 函数
    # last_message = input.history[-1].content
    results = similarity_search(input, 10)
    return results

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)

