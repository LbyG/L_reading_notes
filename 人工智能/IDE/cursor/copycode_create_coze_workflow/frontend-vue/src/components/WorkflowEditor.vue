<template>
  <div class="workflow-editor">
    <!-- 顶部栏 -->
    <div class="top-bar">
      <div class="workflow-title">
        <div class="workflow-icon">W</div>
        <input
          v-model="workflowName"
          type="text"
          placeholder="未命名工作流"
          class="workflow-name-input"
        />
      </div>
      <div class="divider"></div>
      <div class="flex-spacer"></div>
      <button class="primary-button" @click="handleSave">
        <span class="icon">+</span>
        保存工作流
      </button>
    </div>

    <!-- 流程图区域 -->
    <VueFlow
      v-model="elements"
      :default-viewport="{ x: 0, y: 0, zoom: 1 }"
      :default-edge-options="defaultEdgeOptions"
      class="workflow-canvas"
      @connect="onConnect"
      @dragover="onDragOver"
      @drop="onDrop"
    >
      <template #node-start="nodeProps">
        <StartNode v-bind="nodeProps" />
      </template>

      <Background pattern="dots" :gap="12" :size="1" />
      <MiniMap />
      <Controls />
    </VueFlow>

    <!-- 底部面板 -->
    <div class="bottom-panel">
      <button class="primary-button" @click="handleOptimizeLayout">
        优化布局
      </button>
      <button class="primary-button" @click="toggleNodePopover">
        <span class="icon">+</span>
        添加节点
      </button>
      <div class="zoom-controls">
        <button class="zoom-button" @click="handleZoom(-0.2)">-</button>
        <span class="zoom-value">{{ Math.round(zoom * 100) }}%</span>
        <button class="zoom-button" @click="handleZoom(0.2)">+</button>
      </div>
    </div>

    <!-- 节点选择弹出层 -->
    <div v-if="showNodePopover" class="node-popover">
      <div v-for="(nodes, category) in nodeCategories" :key="category" class="node-category">
        <h3>{{ category }}</h3>
        <div class="node-grid">
          <div
            v-for="node in nodes"
            :key="node.type"
            class="node-item"
            draggable
            @dragstart="onDragStart($event, node)"
            @click="handleAddNode(node.type, node.color)"
          >
            <span class="node-icon" :style="{ background: node.color }">
              {{ node.icon }}
            </span>
            <span class="node-label">{{ node.label }}</span>
          </div>
        </div>
      </div>
    </div>

    <!-- 保存提示 -->
    <transition name="fade">
      <div
        v-if="saveMessage"
        class="save-message"
        :class="{ success: saveMessage.type === 'success' }"
      >
        <span class="icon">{{ saveMessage.type === 'success' ? '✓' : '✕' }}</span>
        {{ saveMessage.text }}
      </div>
    </transition>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue'
import {
  VueFlow,
  Background,
  MiniMap,
  Controls,
  useVueFlow,
  Position,
} from '@vue-flow/core'
import '@vue-flow/core/dist/style.css'
import '@vue-flow/core/dist/theme-default.css'
import dagre from 'dagre'
import StartNode from './nodes/StartNode.vue'
import ImageClassificationNode from './nodes/ImageClassificationNode.vue'
import LargeModelNode from './nodes/LargeModelNode.vue'
import CodeNode from './nodes/CodeNode.vue'
import LoopNode from './nodes/LoopNode.vue'
import ApiNode from './nodes/ApiNode.vue'
import IntentRecognitionNode from './nodes/IntentRecognitionNode.vue'
import { nodeCategories, defaultEdgeOptions } from '../config/nodeTypes'

export default defineComponent({
  name: 'WorkflowEditor',
  components: {
    VueFlow,
    Background,
    MiniMap,
    Controls,
    StartNode,
  },
  setup() {
    const workflowName = ref('未命名工作流')
    const elements = ref([])
    const zoom = ref(1)
    const showNodePopover = ref(false)
    const saveMessage = ref(null)

    const { project, addNodes, addEdges, setTransform } = useVueFlow()

    const handleSave = async () => {
      try {
        const workflowData = {
          name: workflowName.value,
          nodes: elements.value.filter(el => el.type !== 'edge'),
          edges: elements.value.filter(el => el.type === 'edge'),
          lastModified: new Date().toISOString(),
        }
        
        const response = await fetch('http://localhost:5001/api/workflow', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          mode: 'cors',
          body: JSON.stringify(workflowData),
        })
        
        const data = await response.json()
        
        if (data.success) {
          showSaveMessage('success', '工作流保存成功')
        } else {
          throw new Error(data.message || '保存失败')
        }
      } catch (error) {
        console.error('Save error:', error)
        showSaveMessage('error', `保存失败: ${error.message}`)
      }
    }

    const showSaveMessage = (type: 'success' | 'error', text: string) => {
      saveMessage.value = { type, text }
      setTimeout(() => {
        saveMessage.value = null
      }, 3000)
    }

    const handleOptimizeLayout = () => {
      const g = new dagre.graphlib.Graph()
      g.setGraph({
        rankdir: 'LR',
        nodesep: 80,
        ranksep: 100,
        marginx: 20,
        marginy: 20,
      })
      g.setDefaultEdgeLabel(() => ({}))

      const nodes = elements.value.filter(el => el.type !== 'edge')
      const edges = elements.value.filter(el => el.type === 'edge')

      nodes.forEach((node) => {
        g.setNode(node.id, { width: 180, height: 40 })
      })

      edges.forEach((edge) => {
        g.setEdge(edge.source, edge.target)
      })

      dagre.layout(g)

      const optimizedNodes = nodes.map((node) => {
        const nodeWithPosition = g.node(node.id)
        return {
          ...node,
          position: {
            x: nodeWithPosition.x - nodeWithPosition.width / 2,
            y: nodeWithPosition.y - nodeWithPosition.height / 2,
          },
        }
      })

      elements.value = [...optimizedNodes, ...edges]
      showSaveMessage('success', '布局优化完成')
    }

    const handleZoom = (delta: number) => {
      const newZoom = Math.max(0.1, Math.min(2, zoom.value + delta))
      zoom.value = newZoom
      setTransform({ zoom: newZoom })
    }

    const toggleNodePopover = () => {
      showNodePopover.value = !showNodePopover.value
    }

    const onDragStart = (event: DragEvent, node: any) => {
      if (event.dataTransfer) {
        event.dataTransfer.setData('application/nodeType', node.type)
        event.dataTransfer.setData('application/nodeColor', node.color)
        event.dataTransfer.effectAllowed = 'move'
      }
    }

    const onDragOver = (event: DragEvent) => {
      event.preventDefault()
      if (event.dataTransfer) {
        event.dataTransfer.dropEffect = 'move'
      }
    }

    const onDrop = (event: DragEvent) => {
      event.preventDefault()

      if (!event.dataTransfer) return

      const type = event.dataTransfer.getData('application/nodeType')
      const color = event.dataTransfer.getData('application/nodeColor')
      
      if (!type || !project) return

      const position = project({
        x: event.clientX,
        y: event.clientY,
      })

      handleAddNode(type, color, position)
    }

    const handleAddNode = (type: string, color: string, position?: { x: number; y: number }) => {
      const id = getId()
      const newNode = {
        id: `${id}`,
        type,
        position: position || {
          x: Math.random() * 500,
          y: Math.random() * 500,
        },
        data: { 
          label: id,
          ...(type === 'code' && { outputs: ['key0', 'key1', 'key2'] }),
          ...(type === 'imageClassification' && { 
            query: '未配置查询',
            outputs: ['classificationId', 'reason']
          }),
          ...(type === 'largeModel' && {
            modelType: '官方工具调用',
            function: '未配置功能'
          }),
          ...(type === 'intentRecognition' && {
            intent: '未配置意图',
            confidence: 0.0
          })
        }
      }

      elements.value = [...elements.value, newNode]
      if (!position) {
        showNodePopover.value = false
      }
    }

    const onConnect = (params: any) => {
      const edge = {
        id: `e${getId()}`,
        source: params.source,
        target: params.target,
        type: 'smoothstep',
        animated: true,
      }
      elements.value = [...elements.value, edge]
    }

    const nodeTypes = {
      start: StartNode,
      code: CodeNode,
      loop: LoopNode,
      api: ApiNode,
      imageClassification: ImageClassificationNode,
      largeModel: LargeModelNode,
      intentRecognition: IntentRecognitionNode,
    }

    const initialNodes = [
      {
        id: '1',
        type: 'start',
        position: { x: 50, y: 200 },
        data: { label: '开始' }
      },
      {
        id: '2',
        type: 'code',
        position: { x: 250, y: 300 },
        data: { label: '5' }
      },
      {
        id: '3',
        type: 'loop',
        position: { x: 450, y: 300 },
        data: { label: '6' }
      },
      {
        id: '4',
        type: 'api',
        position: { x: 250, y: 100 },
        data: { label: '4' }
      },
      {
        id: '5',
        type: 'start',
        position: { x: 650, y: 200 },
        data: { label: '结束' }
      }
    ]

    const initialEdges = [
      {
        id: 'e1-2',
        source: '1',
        target: '2',
        type: 'smoothstep',
        animated: true
      },
      {
        id: 'e1-4',
        source: '1',
        target: '4',
        type: 'smoothstep',
        animated: true
      },
      {
        id: 'e2-3',
        source: '2',
        target: '3',
        type: 'smoothstep',
        animated: true
      },
      {
        id: 'e3-5',
        source: '3',
        target: '5',
        type: 'smoothstep',
        animated: true
      },
      {
        id: 'e4-5',
        source: '4',
        target: '5',
        type: 'smoothstep',
        animated: true
      }
    ]

    onMounted(() => {
      elements.value = [...initialNodes, ...initialEdges]
    })

    return {
      workflowName,
      elements,
      zoom,
      showNodePopover,
      saveMessage,
      nodeCategories,
      defaultEdgeOptions,
      handleSave,
      handleOptimizeLayout,
      handleZoom,
      toggleNodePopover,
      onDragStart,
      onDragOver,
      onDrop,
      onConnect,
      nodeTypes,
    }
  }
})
</script>

<style lang="scss" scoped>
.workflow-editor {
  width: 100vw;
  height: 100vh;
  position: relative;
  background: #f5f5f5;
}

.workflow-canvas {
  width: 100%;
  height: 100%;
}

.top-bar {
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
}

.workflow-title {
  display: flex;
  align-items: center;
  gap: 8px;
}

.workflow-icon {
  width: 32px;
  height: 32px;
  background: #E8F5E9;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #2E7D32;
  font-size: 16px;
}

.workflow-name-input {
  padding: 8px 12px;
  font-size: 14px;
  border: none;
  outline: none;
  width: 200px;

  &:focus {
    background: #f5f5f5;
    border-radius: 4px;
  }
}

.divider {
  width: 1px;
  height: 24px;
  background: #E0E0E0;
}

.flex-spacer {
  flex: 1;
}

.primary-button {
  padding: 6px 16px;
  background: #6E56CF;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 13px;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: background 0.2s;

  &:hover {
    background: #5B46B0;
  }

  .icon {
    font-size: 16px;
  }
}

.bottom-panel {
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
}

.zoom-controls {
  display: flex;
  gap: 8px;
  align-items: center;
}

.zoom-button {
  padding: 6px 12px;
  border: 1px solid #ddd;
  background: white;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s;

  &:hover {
    background: #f5f5f5;
  }
}

.zoom-value {
  padding: 6px 12px;
  min-width: 60px;
  text-align: center;
}

.node-popover {
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
}

.node-category {
  margin-bottom: 16px;

  &:last-child {
    margin-bottom: 0;
  }

  h3 {
    font-size: 13px;
    color: #666;
    margin: 0 0 8px 0;
    padding-bottom: 8px;
    border-bottom: 1px solid #eee;
  }
}

.node-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
}

.node-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  padding: 12px;
  border: 1px solid #eee;
  border-radius: 6px;
  cursor: grab;
  transition: all 0.2s;

  &:hover {
    background: #f5f5f5;
    border-color: #ddd;
    transform: translateY(-1px);
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
  }

  &:active {
    cursor: grabbing;
  }
}

.node-icon {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 6px;
  color: white;
  font-size: 16px;
}

.node-label {
  font-size: 13px;
  color: #333;
  text-align: center;
}

.save-message {
  position: fixed;
  top: 20px;
  right: 20px;
  padding: 12px 20px;
  background: #F44336;
  color: white;
  border-radius: 4px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.2);
  display: flex;
  align-items: center;
  gap: 8px;
  z-index: 1000;
  animation: slideIn 0.3s ease;

  &.success {
    background: #4CAF50;
  }
}

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

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style> 