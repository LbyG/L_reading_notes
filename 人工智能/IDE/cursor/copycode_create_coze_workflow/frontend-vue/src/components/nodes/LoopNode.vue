<template>
  <div class="node-wrapper">
    <div class="node-content">
      循环_{{ data.label }}
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
  name: 'LoopNode',
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
  background: #9C27B0;
  border-radius: 4px;
  min-width: 120px;
  position: relative;
}

.node-content {
  padding: 8px 16px;
  color: white;
  font-size: 14px;
  text-align: center;
}
</style> 