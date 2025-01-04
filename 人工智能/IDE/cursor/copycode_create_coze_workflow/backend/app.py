from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import json
import os
from datetime import datetime

app = FastAPI()

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 确保存储目录存在
WORKFLOWS_DIR = 'workflows'
if not os.path.exists(WORKFLOWS_DIR):
    os.makedirs(WORKFLOWS_DIR)

# 定义数据模型
class Position(BaseModel):
    x: float
    y: float

class NodeStyle(BaseModel):
    background: str
    color: str
    border: Optional[str] = None
    borderRadius: Optional[str] = None
    padding: Optional[str] = None

class NodeData(BaseModel):
    label: str

class Node(BaseModel):
    id: str
    type: str
    position: Position
    data: NodeData
    style: NodeStyle
    sourcePosition: Optional[str] = None
    targetPosition: Optional[str] = None

class Edge(BaseModel):
    id: Optional[str] = None
    source: str
    target: str
    type: Optional[str] = None
    animated: Optional[bool] = None
    style: Optional[Dict[str, Any]] = None
    markerEnd: Optional[Dict[str, Any]] = None

class Workflow(BaseModel):
    name: str
    nodes: List[Node]
    edges: List[Edge]
    lastModified: datetime

@app.post("/api/workflow")
async def save_workflow(workflow: Workflow):
    try:
        # 处理文件名，移除不合法字符
        safe_name = "".join([c for c in workflow.name if c.isalnum() or c in (' ', '_', '-')]).rstrip()
        if not safe_name:
            safe_name = 'untitled'
            
        # 保存到文件
        filename = f"{WORKFLOWS_DIR}/{safe_name}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(workflow.dict(), f, ensure_ascii=False, indent=2, default=str)
        
        return {
            "success": True,
            "message": "工作流保存成功",
            "filename": filename
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/workflow/{name}")
async def get_workflow(name: str):
    try:
        safe_name = "".join([c for c in name if c.isalnum() or c in (' ', '_', '-')]).rstrip()
        filename = f"{WORKFLOWS_DIR}/{safe_name}.json"
        
        if not os.path.exists(filename):
            raise HTTPException(status_code=404, detail="工作流不存在")
            
        with open(filename, 'r', encoding='utf-8') as f:
            workflow = json.load(f)
            
        return workflow

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/workflows")
async def list_workflows():
    try:
        workflows = []
        for filename in os.listdir(WORKFLOWS_DIR):
            if filename.endswith('.json'):
                with open(os.path.join(WORKFLOWS_DIR, filename), 'r', encoding='utf-8') as f:
                    workflow = json.load(f)
                    workflows.append({
                        'name': workflow['name'],
                        'lastModified': workflow['lastModified']
                    })
        return workflows
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5001)