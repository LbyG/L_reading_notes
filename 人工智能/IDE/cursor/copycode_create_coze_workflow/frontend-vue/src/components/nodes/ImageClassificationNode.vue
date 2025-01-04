<template>
  <BaseNode
    type="图像识别"
    :data="data"
    :selected="selected"
    color="#00BFA5"
    icon="🖼"
    :inputs="['query']"
    :outputs="['classificationId', 'reason']"
  >
    <template #content>
      <div class="node-content">
        <div class="input-row">
          <span class="label">输入</span>
          <span class="value">{{ data.query || '未配置查询' }}</span>
        </div>
        <div class="output-row">
          <div class="output-item">
            <span class="label">分类ID</span>
            <span class="type">str</span>
          </div>
          <div class="output-item">
            <span class="label">原因</span>
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
  name: 'ImageClassificationNode',
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

.input-row,
.output-row {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.output-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 4px 8px;
  background: #f5f5f5;
  border-radius: 4px;
}

.label {
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
  background: #00BFA5;
  color: white;
  border-radius: 3px;
  font-size: 11px;
}
</style> 