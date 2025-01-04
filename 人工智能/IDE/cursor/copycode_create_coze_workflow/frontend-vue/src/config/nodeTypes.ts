export const nodeCategories = {
  '基础节点': [
    {
      type: 'start',
      label: '开始/结束',
      icon: '▶',
      color: '#4CAF50',
    }
  ],
  '功能节点': [
    {
      type: 'code',
      label: '代码',
      icon: '</>',
      color: '#00BCD4',
    },
    {
      type: 'loop',
      label: '循环',
      icon: '⟲',
      color: '#9C27B0',
    },
    {
      type: 'api',
      label: '接口',
      icon: '⚡',
      color: '#795548',
    }
  ],
  'AI节点': [
    {
      type: 'imageClassification',
      label: '图像识别',
      icon: '🖼',
      color: '#00BFA5',
    },
    {
      type: 'largeModel',
      label: '大模型',
      icon: '🤖',
      color: '#5C6BC0',
    },
    {
      type: 'intentRecognition',
      label: '意图识别',
      icon: '🎯',
      color: '#FF5722',
    }
  ]
}

export const defaultEdgeOptions = {
  type: 'smoothstep',
  animated: true,
  style: {
    stroke: '#6366F1',
    strokeWidth: 2,
    strokeDasharray: '5,5'
  }
} 