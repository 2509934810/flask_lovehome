<template>
  <div>
    <div class="banner container">
      <div class="item">
        <img :src="midPhoto" width="100%" height="400px">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'mid',
  data () {
    return {
      data: {
        midPhoto: '#'
      }
    }
  },
  created () {
    this.midPhoto = require('@' + '/assets/JiaZheng.jpeg')
  }
}
</script>
<style lang="">
  .container{width: 80%; margin: 0 auto}
  .banner{margin-top: 20px}
  ul{list-style: none}
  li{float: left}
</style>
