<template>
  <BaseNode
    type="大模型"
    :data="data"
    :selected="selected"
    color="#5C6BC0"
    icon="🤖"
    :inputs="['input']"
    :outputs="['output']"
  >
    <template #content>
      <div class="node-content">
        <div class="model-info">
          <div class="info-row">
            <span class="label">输入</span>
            <span class="value">未配置输入</span>
          </div>
          <div class="info-row">
            <span class="label">输出</span>
            <span class="type">str</span>
          </div>
          <div class="info-row">
            <span class="label">模型</span>
            <span class="model-type">官方工具调用</span>
          </div>
          <div class="info-row">
            <span class="label">功能</span>
            <span class="value">未配置内容</span>
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
  name: 'LargeModelNode',
  components: { BaseNode },
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
.node-content {
  padding: 8px;
}

.model-info {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.info-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 4px 8px;
  background: #f5f5f5;
  border-radius: 4px;
  font-size: 12px;
}

.label {
  color: #666;
}

.value {
  color: #999;
  font-style: italic;
}

.type {
  padding: 2px 6px;
  background: #5C6BC0;
  color: white;
  border-radius: 3px;
  font-size: 11px;
}

.model-type {
  padding: 2px 6px;
  background: #E8EAF6;
  color: #5C6BC0;
  border-radius: 3px;
  font-size: 11px;
}
</style> 