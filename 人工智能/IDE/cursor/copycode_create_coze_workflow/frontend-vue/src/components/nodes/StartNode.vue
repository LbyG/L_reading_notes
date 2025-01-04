<template>
  <BaseNode
    type="开始"
    :data="data"
    :selected="selected"
    color="#6C5CE7"
    icon="▶"
    :outputs="['output']"
  >
    <template #content>
      <div class="start-content">
        <div class="input-config">
          <span class="label">输入参数</span>
          <div class="param-type">
            <span class="type">str</span>
            <span class="status">未定义</span>
          </div>
        </div>
      </div>
    </template>
  </BaseNode>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import BaseNode from './BaseNode.vue'

export default defineComponent({
  name: 'StartNode',
  components: {
    BaseNode
  },
  props: {
    data: {
      type: Object,
      required: true
    },
    selected: {
      type: Boolean,
      default: false
    }
  }
})
</script>

<style lang="scss" scoped>
.start-content {
  padding: 8px;
}

.input-config {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 6px 8px;
  background: #f5f5f5;
  border-radius: 4px;
  font-size: 12px;
}

.label {
  color: #666;
}

.param-type {
  display: flex;
  align-items: center;
  gap: 4px;
}

.type {
  padding: 2px 6px;
  background: #6C5CE7;
  color: white;
  border-radius: 3px;
  font-size: 11px;
}

.status {
  color: #999;
  font-style: italic;
  font-size: 11px;
}
</style> 