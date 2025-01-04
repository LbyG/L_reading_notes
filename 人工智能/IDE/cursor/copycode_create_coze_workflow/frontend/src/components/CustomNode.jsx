import React from 'react';
import { Handle, Position } from 'reactflow';
import styled from 'styled-components';

const NodeWrapper = styled.div`
  padding: 16px;
  border-radius: 8px;
  background: white;
  border: 1px solid #e0e0e0;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  width: 200px;
`;

const StartNode = styled(NodeWrapper)`
  display: flex;
  align-items: center;
  gap: 12px;
`;

const IconWrapper = styled.div`
  width: 32px;
  height: 32px;
  background: #6C5CE7;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 18px;
`;

const NodeContent = styled.div`
  flex: 1;
`;

const NodeLabel = styled.div`
  font-size: 14px;
  color: #333;
`;

const NodeInput = styled.div`
  margin-top: 4px;
  font-size: 12px;
  color: #999;
  display: flex;
  align-items: center;
  gap: 4px;
`;

function CustomNode({ data }) {
  return (
    <StartNode>
      <IconWrapper>G</IconWrapper>
      <NodeContent>
        <NodeLabel>{data.label}</NodeLabel>
        <NodeInput>
          <span>输入</span>
          <span style={{ color: '#ccc' }}>str 未定义</span>
        </NodeInput>
      </NodeContent>
      <Handle
        type="source"
        position={Position.Right}
        style={{
          background: '#6C5CE7',
          width: 8,
          height: 8,
          border: 'none',
        }}
      />
    </StartNode>
  );
}

export default CustomNode;