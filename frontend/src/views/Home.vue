<template>
  <div class="home">
    <Base/>
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  </div>
</template>

<script>
// @ is an alias to /src
import Base from '@/components/Base.vue'
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'home',
  components: {
    Base
  }
}
</script>
