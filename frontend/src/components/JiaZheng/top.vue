<template>
  <div id="top">
    <div id="logo" class="l">
      <a>
        <img src="@/assets/index-logo.jpg" alt="lovehome" width="45" height="45px" border-radius="10px">
      </a>
    </div>
    <div id="top_title">
      <!-- <h2>我爱我家家政服务安全发布平台</h2> -->
    </div>
    <div id="menu" class="l">
      <ul>
        <li><a v-bind:href="BACKEND_API">首页</a></li>
        <li><a href="/#/homeservice">家政</a></li>
        <li><a href="#">月嫂</a></li>
        <li><a href="#">租房</a></li>
        <li><a href="#">技术支持</a></li>
      </ul>
    </div>
    <div class="Loginmenu r">
      <ul>
        <li><a v-bind:href="LOGIN_URL">登陆</a></li>
        <li><a v-bind:href="REGISTRY_URL">注册</a></li>
      </ul>
    </div>
  </div>
</template>

<script>
const BaseHost = process.env.BACKEND_API
export default {
  name: 'top',
  data () {
    return {
      BACKEND_API: '#',
      LOGIN_URL: '#',
      REGISTRY_URL: '#'
    }
  },
  created () {
    this.BACKEND_API = BaseHost
    this.LOGIN_URL = BaseHost + '/auth/login'
    this.REGISTRY_URL = BaseHost + '/auth/register'
  }
}
</script>

<style>

</style>
