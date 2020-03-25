<template>
  <div class="service container">
    <h1>service</h1>
    <div class="WorkerInfo">
      <ul>
        <li v-for="data in dataList" :key="data.id">
          <div>
             {{ data }}
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'service',
  data () {
    return {
      msg: '#',
      dataList: ['worker1', 'worker1', 'worker1', 'worker1']
    }
  }
}
</script>
<style lang="">
  .container{width: 90%; margin: 0 auto;}
  .service{}
</style>
