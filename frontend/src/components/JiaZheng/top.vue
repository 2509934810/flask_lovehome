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
        <li><router-link to="/">首页</router-link></li>
        <li><router-link to="/homeservice">家政</router-link></li>
        <li><a href="#">月嫂</a></li>
        <li><a href="#">租房</a></li>
        <li><a href="#">技术支持</a></li>
        <router-view></router-view>
      </ul>
    </div>
    <div class="Loginmenu r">
      <div v-if="nologin">
        <ul>
          <li><router-link to="/login">登陆</router-link></li>
          <li><router-link to="/register">注册</router-link></li>
          <router-view></router-view>
        </ul>
      </div>
      <div v-else>
        <ul>
          <li><a v-on:click="logout" href="#">注销</a></li>
          <li><a v-bind:href="myInfoRouter">我的信息</a></li>
          <router-view></router-view>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
const BaseHost = process.env.BACKEND_API
// import router from './../../router'
// import axios from 'axios'
export default {
  name: 'top',
  data () {
    return {
      BACKEND_API: '#',
      LOGIN_URL: '#',
      REGISTRY_URL: '#',
      nologin: true,
      myInfoRouter: '#'
    }
  },
  created () {
    this.BACKEND_API = BaseHost
    this.LOGIN_URL = BaseHost + '/auth/login'
    this.REGISTRY_URL = BaseHost + '/auth/register'
    if (localStorage.length > 0) {
      if (localStorage.getItem('user')) {
        this.nologin = false
      }
    }
    let useraccount = JSON.parse(localStorage.getItem('user')).account
    this.myInfoRouter = '/#/user/' + useraccount
  },
  methods: {
    logout () {
      localStorage.removeItem('user')
      location.reload()
      // axios({
      //   method: 'get',
      //   url: this.
      // })
    }
  }
}
</script>

<style>
*{margin: 0; padding: 0;}
a{text-decoration: none;}
ul, ol{list-style: none;}
.container{width:100%; margin:0 auto; position: relative;}
.container-fluid{width: 100%;}
img{display: block;}
h1, h2, h3{ font-size: 16px;}
.clear:after{ content: ''; clear:both; display: block;}

.l{float: left;}
.r{float: right;}
body{background-color: lightyellow;}
#top{height: 60px; margin-top: 2px; min-width: 480px; position: relative; font-weight: bold;}
#logo{width: 40; height: 40px; margin-top: 10px; margin-left: 30px;}

#menu{line-height: 60px; font-size: 20px; margin-left: 90px;}
#menu li{float: left; margin-left: 20px;}
#menu a{color: black; font-weight: bold;}
#menu a:nth-child(1){margin-left: 80px;}

#top .Loginmenu{line-height: 60px; margin-right: 20px;}
#top .Loginmenu li{float: right; margin-left: 20px;}
#top .title{margin: 0 auto; height: 60px; line-height: 60px; width: 400px;}
#top .title p{font-size: 30px;}
#top .MainInfo{width: 100px; position: relative; right: 30px; top: -45px; line-height: 50px;}
#top .MainInfo ul {display: none;}
#top .MainInfo:hover ul{display: block;}
#top .MainInfo li a{display: block; width: 100%; height: 100%; text-align: center;}
#top .MainInfo li:hover {background-color: gray;}
</style>
