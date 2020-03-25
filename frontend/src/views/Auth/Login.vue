<template>
  <div>
    <top></top>
    <div></div>
    <div class="loginForm">
      <div class="formTitle">
        <h1>登&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;陆</h1>
      </div>
      <div class="inputInfo">
        <label for="username">用户名:</label>
        <input type="text" v-model="username" id="username" required>
      </div>
      <div class="inputInfo">
        <label for="password">密&nbsp;&nbsp;&nbsp;码:</label>
        <input type="password" v-model="password" id="password" required>
      </div>
      <div class="loginButton">
        <input type="button" v-on:click="Login" value="Login">
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import top from '@/components/JiaZheng/top.vue'
import router from './../../router'
export default {
  name: 'login',
  data () {
    return {
      msg: '3',
      username: '',
      password: ''
    }
  },
  components: {
    top
  },
  methods: {
    Login () {
      console.log(this.username)
      console.log(process.env.BACKEND_API + 'api/login')
      if (this.username === '' && this.password === '') {
        alert('请完善信息')
      } else {
        console.log('send msg')
        axios({
          method: 'post',
          url: process.env.BACKEND_API + 'api/login',
          data: {
            username: this.username,
            password: this.password
          }
        }).then(function (res) {
          console.log(res.data.code, res.data.debugInfo)
          if (res.data.code === 200) {
            const userData = res.data
            localStorage.setItem('user', JSON.stringify(userData))
            // console.log(router.current.path)
            router.push({name: 'index'})
          }
        })
      }
    }
  }
}
</script>
<style lang="">
  body{margin: 0; background-color: lightyellow;}
  .formTitle{margin-top: 30px; font-size: 19px;}
  ul{list-style: none;}
  .loginForm{width: 25%; margin: 0 auto; margin-top: 100px; background-color: lightgreen; height: 300px; border-radius: 20px}
  .inputInfo input{width: 60%; height: 30px; font-size: 25px; margin-top: 30px;}
  .loginButton input{width: 50%; height: 30px; display: block; border-radius: 5px; margin: 0 auto; margin-top: 40px;}
  .loginButton input:hover{border: 1px solid blue;}
</style>
