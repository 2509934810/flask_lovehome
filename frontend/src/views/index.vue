<template>
  <div>
    <top></top>
    <div id="banner" class="container-fluid">
      <ul class="banner_list">
        <li>
          <img v-bind:src="bannerpath" width="100%">
        </li>
      </ul>
    </div>
    <show></show>
    <foot></foot>
  </div>
</template>
<script>
import top from '@/components/JiaZheng/top.vue'
import ad from '@/components/Index/Ad.vue'
import foot from '@/components/JiaZheng/foot.vue'
import show from '@/components/Index/show.vue'
export default {
  name: 'index',
  data () {
    return {
      msg: '#',
      bannerpath: '#'
    }
  },
  created () {
    this.bannerpath = require('@' + '/assets/banner.jpg')
  },
  components: {
    top,
    ad,
    foot,
    show
  }
}
</script>
<style lang="">
  .container-fluid{width: 100%;}
  #banner{margin-top: 10px;}
  .banner_list{width: 95%; margin: 0 auto;}
</style>
