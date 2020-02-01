<template>
  <!-- 创建要控制的区域 -->
  <div id="app">
    <div class="panel panel-primary">
      <div class="panel-heading">
        <h3 class="panel-title">Add Product</h3>
      </div>
      <div class="panel-body form-inline">
        <label>
          Id:
          <input type="text" class="form-control" v-model="id">
        </label>
        <label>
          Name:
          <input type="text" class="form-control" v-model="name" @keyup.enter="add">
        </label>
        <label>Keywords Search:
          <input type="text" class="form-control" v-model="keywords">
        </label>
        <input type="button" value="Add" class="btn btn-primary" @click="add">
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'Product'
}
</script>

<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
