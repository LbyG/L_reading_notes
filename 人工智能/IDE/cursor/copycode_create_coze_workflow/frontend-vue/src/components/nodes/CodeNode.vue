<template>
  <BaseNode
    type="代码"
    :data="data"
    :selected="selected"
    color="#7E57C2"
    icon="</>"
    :inputs="['input']"
    :outputs="['key0', 'key1', 'key2']"
  >
    <template #content>
      <div class="node-content">
        <div class="input-section">
          <span class="label">输入</span>
          <span class="value">未配置输入</span>
        </div>
        <div class="output-section">
          <div class="output-row" v-for="key in ['key0', 'key1', 'key2']" :key="key">
            <span class="key">{{ key }}</span>
            <span class="type">str</span>
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
  name: 'CodeNode',
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
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.input-section,
.output-section {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.input-section {
  padding: 4px 8px;
  background: #f5f5f5;
  border-radius: 4px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.output-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 4px 8px;
  background: #f5f5f5;
  border-radius: 4px;
}

.label,
.key {
  color: #666;
  font-size: 12px;
}

.value {
  color: #999;
  font-size: 12px;
  font-style: italic;
}

.type {
  padding: 2px 6px;
  background: #7E57C2;
  color: white;
  border-radius: 3px;
  font-size: 11px;
}
</style> 