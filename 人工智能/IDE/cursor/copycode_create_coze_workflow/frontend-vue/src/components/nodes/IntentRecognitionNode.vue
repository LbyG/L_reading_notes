<template>
  <div class="node-wrapper">
    <div class="node-content">
      <div class="info-row">
        <span class="label">意图</span>
        <span class="value">{{ data.intent || '未配置意图' }}</span>
      </div>
      <div class="info-row">
        <span class="label">置信度</span>
        <span class="confidence">{{ (data.confidence || 0).toFixed(2) }}</span>
      </div>
    </div>
    <Handle
      type="target"
      position="left"
      :style="handleStyle"
    />
    <Handle
      type="source"
      position="right"
      :style="handleStyle"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent, computed } from 'vue'
import { Handle } from '@vue-flow/core'

export default defineComponent({
  name: 'IntentRecognitionNode',
  components: { Handle },
  props: {
    data: {
      type: Object,
      required: true
    }
  },
  setup() {
    const handleStyle = computed(() => ({
      background: '#6E56CF',
      width: '8px',
      height: '8px',
      border: 'none',
    }))

    return {
      handleStyle
    }
  }
})
</script>

<style lang="scss" scoped>
.node-wrapper {
  background: #FF5722;
  border-radius: 4px;
  min-width: 120px;
  position: relative;
}

.node-content {
  padding: 8px;
  color: white;
  font-size: 14px;
}

.info-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 4px 8px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 4px;
  margin-bottom: 4px;

  &:last-child {
    margin-bottom: 0;
  }
}

.label {
  font-size: 12px;
  opacity: 0.8;
}

.value {
  font-size: 12px;
}

.confidence {
  background: rgba(255, 255, 255, 0.2);
  padding: 2px 6px;
  border-radius: 3px;
  font-size: 11px;
}
</style> 