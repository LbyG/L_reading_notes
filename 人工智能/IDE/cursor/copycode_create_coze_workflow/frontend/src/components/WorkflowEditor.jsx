import React, { useState, useCallback, useRef, useEffect } from 'react';
import ReactFlow, {
  addEdge,
  MiniMap,
  Controls,
  Background,
  useNodesState,
  useEdgesState,
  Position,
  MarkerType,
} from 'reactflow';
import styled from 'styled-components';
import 'reactflow/dist/style.css';
import dagre from 'dagre';
import CustomNode from './CustomNode';

const TopBar = styled.div`
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 48px;
  background: white;
  display: flex;
  align-items: center;
  padding: 0 20px;
  box-shadow: 0 1px 2px rgba(0,0,0,0.1);
  z-index: 5;
  gap: 16px;
`;

const WorkflowTitle = styled.div`
  display: flex;
  align-items: center;
  gap: 8px;
`;

const WorkflowIcon = styled.div`
  width: 32px;
  height: 32px;
  background: #E8F5E9;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #2E7D32;
  font-size: 16px;
`;

const Divider = styled.div`
  width: 1px;
  height: 24px;
  background: #E0E0E0;
`;

const BottomPanel = styled.div`
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  display: flex;
  padding: 8px;
  gap: 12px;
  z-index: 5;
  align-items: center;
`;

const ZoomButton = styled.button`
  padding: 6px 12px;
  border: 1px solid #ddd;
  background: white;
  border-radius: 4px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 4px;
  
  &:hover {
    background: #f5f5f5;
  }
`;

const NodePopover = styled.div`
  position: absolute;
  bottom: 80px;
  left: 50%;
  transform: translateX(-50%);
  background: white;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  padding: 16px;
  z-index: 1000;
  width: 480px;
`;

const NodeGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  margin-top: 12px;
`;

const NodeCategory = styled.div`
  margin-bottom: 16px;

  h3 {
    font-size: 13px;
    color: #666;
    margin: 0 0 8px 0;
    padding-bottom: 8px;
    border-bottom: 1px solid #eee;
  }
`;

const NodeItem = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  padding: 12px;
  border: 1px solid #eee;
  border-radius: 6px;
  background: white;
  cursor: grab;
  transition: all 0.2s;
  user-select: none;
  
  &:hover {
    background: #f5f5f5;
    border-color: #ddd;
    transform: translateY(-1px);
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
  }

  &:active {
    cursor: grabbing;
  }

  .icon {
    width: 32px;
    height: 32px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 6px;
    color: white;
    font-size: 16px;
  }

  .label {
    font-size: 13px;
    color: #333;
  }
`;

const initialNodes = [];

let id = 3;
const getId = () => `${id++}`;

const defaultEdgeOptions = {
  type: 'bezier',
  animated: true,
  style: {
    stroke: '#6E56CF',
    strokeWidth: 2,
    transition: 'all 0.3s ease'
  },
  markerEnd: {
    type: MarkerType.ArrowClosed,
    color: '#6E56CF',
    width: 20,
    height: 20,
  },
  curvature: 0.3,
};

const SaveMessage = styled.div`
  position: fixed;
  top: 20px;
  right: 20px;
  padding: 12px 20px;
  background: ${props => props.success ? '#4CAF50' : '#F44336'};
  color: white;
  border-radius: 4px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.2);
  display: flex;
  align-items: center;
  gap: 8px;
  z-index: 1000;
  animation: slideIn 0.3s ease;

  @keyframes slideIn {
    from {
      transform: translateX(100%);
      opacity: 0;
    }
    to {
      transform: translateX(0);
      opacity: 1;
    }
  }
`;

function WorkflowEditor() {
  const reactFlowWrapper = useRef(null);
  const [nodes, setNodes, onNodesChange] = useNodesState([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);
  const [workflowName, setWorkflowName] = useState('未命名工作流');
  const [reactFlowInstance, setReactFlowInstance] = useState(null);
  const [zoom, setZoom] = useState(1);
  const [showNodePopover, setShowNodePopover] = useState(false);
  const [saveMessage, setSaveMessage] = useState(null);

  const loadWorkflows = useCallback(async () => {
    try {
      const response = await fetch('http://localhost:5001/api/workflows');
      if (!response.ok) {
        throw new Error('获取工作流列表失败');
      }
      const workflows = await response.json();
      
      if (workflows.length > 0) {
        const latestWorkflow = workflows.sort((a, b) => 
          new Date(b.lastModified) - new Date(a.lastModified)
        )[0];

        const workflowResponse = await fetch(`http://localhost:5001/api/workflow/${encodeURIComponent(latestWorkflow.name)}`);
        if (!workflowResponse.ok) {
          throw new Error('加载工作流失败');
        }
        const workflowData = await workflowResponse.json();
        
        setWorkflowName(workflowData.name);
        setNodes(workflowData.nodes);
        setEdges(workflowData.edges);
      }
    } catch (error) {
      console.error('加载工作流失败:', error);
    }
  }, [setNodes, setEdges]);

  useEffect(() => {
    loadWorkflows();
  }, [loadWorkflows]);

  const onConnect = useCallback(
    (params) => {
      if (params.sourceHandle && params.targetHandle) {
        const sourceHandlePosition = params.sourceHandle.split('__')[1];
        const targetHandlePosition = params.targetHandle.split('__')[1];
        if (sourceHandlePosition === 'right' && targetHandlePosition === 'left') {
          setEdges((eds) => addEdge(params, eds));
        }
      } else {
        setEdges((eds) => addEdge(params, eds));
      }
    },
    [setEdges],
  );

  const onDragOver = useCallback((event) => {
    event.preventDefault();
    event.dataTransfer.dropEffect = 'move';
  }, []);

  const onDrop = useCallback(
    (event) => {
      event.preventDefault();

      const nodeType = event.dataTransfer.getData('application/nodeType');
      const nodeColor = event.dataTransfer.getData('application/nodeColor');
      
      if (!nodeType || !reactFlowInstance) return;

      const position = reactFlowInstance.screenToFlowPosition({
        x: event.clientX,
        y: event.clientY,
      });

      handleAddNode(nodeType, nodeColor, position);
    },
    [reactFlowInstance],
  );

  const handleSave = async () => {
    try {
      const workflowData = {
        name: workflowName,
        nodes: nodes,
        edges: edges,
        lastModified: new Date().toISOString(),
      };
      
      const response = await fetch('http://localhost:5001/api/workflow', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        mode: 'cors',
        body: JSON.stringify(workflowData),
      });
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const data = await response.json();
      
      if (data.success) {
        setSaveMessage({
          type: 'success',
          text: '工作流保存成功'
        });
      } else {
        throw new Error(data.message || '保存失败');
      }
    } catch (error) {
      console.error('Save error:', error);
      setSaveMessage({
        type: 'error',
        text: `保存失败: ${error.message}`
      });
    }

    setTimeout(() => {
      setSaveMessage(null);
    }, 3000);
  };

  const handleZoom = (value) => {
    reactFlowInstance.setZoom(value);
    setZoom(value);
  };

  const nodeCategories = {
    '业务逻辑': [
      { type: 'code', label: '代码', icon: '</>', color: '#00BCD4' },
      { type: 'if', label: '选择器', icon: 'IF', color: '#2196F3' },
      { type: 'loop', label: '循环', icon: '⟲', color: '#9C27B0' },
    ],
    '数据处理': [
      { type: 'data', label: '数据库', icon: '⚡', color: '#FF9800' },
      { type: 'api', label: 'API', icon: '⚙', color: '#795548' },
    ],
    '会话管理': [
      { type: 'chat', label: '会话', icon: '💬', color: '#607D8B' },
    ],
  };

  const handleOptimizeLayout = useCallback(() => {
    const g = new dagre.graphlib.Graph();
    
    // 设置布局方向为从左到右，节点间距
    g.setGraph({
      rankdir: 'LR',
      nodesep: 80,
      ranksep: 100,
      marginx: 20,
      marginy: 20
    });
    
    // 默认节点大小
    g.setDefaultEdgeLabel(() => ({}));
    
    // 添加节点
    nodes.forEach((node) => {
      g.setNode(node.id, { 
        width: 180,
        height: 40 
      });
    });
    
    // 添加边
    edges.forEach((edge) => {
      g.setEdge(edge.source, edge.target);
    });
    
    // 计算布局
    dagre.layout(g);
    
    // 更新节点位置
    const optimizedNodes = nodes.map((node) => {
      const nodeWithPosition = g.node(node.id);
      return {
        ...node,
        position: {
          x: nodeWithPosition.x - nodeWithPosition.width / 2,
          y: nodeWithPosition.y - nodeWithPosition.height / 2,
        },
      };
    });
    
    // 应用新布局
    setNodes(optimizedNodes);

    // 自动适应视图
    setTimeout(() => {
      if (reactFlowInstance) {
        reactFlowInstance.fitView({ padding: 0.2 });
      }
    }, 10);

    // 显示成功提示
    setSaveMessage({
      type: 'success',
      text: '布局优化完成'
    });
    setTimeout(() => {
      setSaveMessage(null);
    }, 3000);
  }, [nodes, edges, reactFlowInstance, setNodes]);

  const nodeTypeNames = {
    'code': '代码',
    'if': '选择器',
    'loop': '循环',
    'data': '数据库',
    'api': '接口',
    'chat': '会话',
  };

  const handleAddNode = (type, color, position) => {
    const typeName = nodeTypeNames[type] || type;
    
    const newNode = {
      id: getId(),
      type: type === 'input' ? 'start' : type,
      position: position || {
        x: Math.random() * 500,
        y: Math.random() * 500,
      },
      data: { 
        label: `${typeName}_${id}`,
      },
      style: type === 'input' ? {} : {
        background: color,
        color: 'white',
        border: 'none',
        borderRadius: '8px',
        padding: '10px 20px',
      },
      sourcePosition: Position.Right,
      targetPosition: Position.Left,
    };

    setNodes((nds) => nds.concat(newNode));
    if (!position) setShowNodePopover(false);
  };

  const onDragStart = (event, nodeType, nodeColor) => {
    event.dataTransfer.setData('application/nodeType', nodeType);
    event.dataTransfer.setData('application/nodeColor', nodeColor);
    event.dataTransfer.effectAllowed = 'move';
  };

  const nodeTypes = {
    start: CustomNode,
  };

  return (
    <div style={{ width: '100vw', height: '100vh' }} ref={reactFlowWrapper}>
      <TopBar>
        <WorkflowTitle>
          <WorkflowIcon>W</WorkflowIcon>
          <input
            type="text"
            value={workflowName}
            onChange={(e) => setWorkflowName(e.target.value)}
            style={{
              padding: '8px 12px',
              fontSize: '14px',
              border: 'none',
              outline: 'none',
              width: '200px',
            }}
          />
        </WorkflowTitle>
        <Divider />
        <div style={{ flex: 1 }} />
        <button 
          onClick={handleSave}
          style={{
            padding: '6px 16px',
            background: '#6E56CF',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: 'pointer',
            fontSize: '13px',
            display: 'flex',
            alignItems: 'center',
            gap: '6px',
          }}
        >
          <span style={{ fontSize: '16px' }}>+</span>
          保存工作流
        </button>
      </TopBar>

      <ReactFlow
        nodes={nodes}
        edges={edges}
        nodeTypes={nodeTypes}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        onInit={setReactFlowInstance}
        onDrop={onDrop}
        onDragOver={onDragOver}
        defaultEdgeOptions={defaultEdgeOptions}
        fitView
      >
        <Controls />
        <MiniMap />
        <Background variant="dots" gap={12} size={1} />
      </ReactFlow>

      <BottomPanel>
        <button
          onClick={handleOptimizeLayout}
          style={{
            padding: '6px 16px',
            background: '#6E56CF',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: 'pointer',
            fontSize: '13px',
            display: 'flex',
            alignItems: 'center',
            gap: '6px',
          }}
        >
          优化布局
        </button>

        <button
          onClick={() => setShowNodePopover(!showNodePopover)}
          style={{
            padding: '6px 16px',
            background: '#6E56CF',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: 'pointer',
            fontSize: '13px',
            display: 'flex',
            alignItems: 'center',
            gap: '6px',
          }}
        >
          <span style={{ fontSize: '16px' }}>+</span>
          添加节点
        </button>

        <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
          <ZoomButton onClick={() => handleZoom(zoom - 0.2)}>
            <span>-</span>
          </ZoomButton>
          <span style={{ padding: '6px 12px' }}>
            {Math.round(zoom * 100)}%
          </span>
          <ZoomButton onClick={() => handleZoom(zoom + 0.2)}>
            <span>+</span>
          </ZoomButton>
        </div>
      </BottomPanel>

      {showNodePopover && (
        <NodePopover>
          {Object.entries(nodeCategories).map(([category, nodes]) => (
            <NodeCategory key={category}>
              <h3>{category}</h3>
              <NodeGrid>
                {nodes.map((node) => (
                  <NodeItem
                    key={node.type}
                    draggable
                    onDragStart={(e) => onDragStart(e, node.type, node.color)}
                    onClick={() => handleAddNode(node.type, node.color)}
                  >
                    <span 
                      className="icon" 
                      style={{ background: node.color }}
                    >
                      {node.icon}
                    </span>
                    <span className="label">{node.label}</span>
                  </NodeItem>
                ))}
              </NodeGrid>
            </NodeCategory>
          ))}
        </NodePopover>
      )}

      {saveMessage && (
        <SaveMessage success={saveMessage.type === 'success'}>
          <span style={{ fontSize: '16px' }}>
            {saveMessage.type === 'success' ? '✓' : '✕'}
          </span>
          {saveMessage.text}
        </SaveMessage>
      )}
    </div>
  );
}

export default WorkflowEditor; 