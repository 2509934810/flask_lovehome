<template>
  <div>
    <div></div>
    <div class="registerForm">
      <div class="formTitle">
        <h1>注&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;册</h1>
      </div>
      <div class="inputInfo">
        <label for="username">名&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;称:</label>
        <input type="text" @blur="checkusername" v-model="username" id="username" required>
        <span>{{info1}}</span>
      </div>
      <div class="inputInfo">
        <label for="account">账&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;号:</label>
        <input type="text" @blur="checkaccount" v-model="account" id="account" required>
        <span>{{info}}</span>
      </div>
      <div class="inputInfo">
        <label for="password">密&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;码:</label>
        <input type="password" v-model="password" id="password" required>
      </div>
      <div class="inputInfo">
        <label for="password2">确认密码:</label>
        <input type="password" @blur="checkpassword" v-model="password2" id="password2" required>
        <span>{{info2}}</span>
      </div>
      <div class="registerButton">
        <button v-on:click="register" >注册</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'register',
  data () {
    return {
      username: '',
      account: '',
      password: '',
      password2: '',
      info: '',
      info1: '',
      info2: ''
    }
  },
  methods: {
    register () {
      if (this.info1 !== '不能为空' && this.info2 !== '密码不匹配' && this.info === '用户可使用') {
        axios({
          method: 'post',
          url: process.env.BACKEND_API + 'api/register',
          data: {
            username: this.username,
            account: this.account,
            password: this.password
          }
        }).then((rsp) => {
          console.log(rsp)
        })
      } else {
        this.info2 = 'some msg are lost'
      }
    },
    checkaccount () {
      if (this.account !== '') {
        if (this.account.length > 12 || this.account.length < 5) {
          this.info = '长度不符合规范'
        } else {
          axios({
            method: 'get',
            url: process.env.BACKEND_API + 'api/findUser/' + this.account
          }).then((rsp) => {
            this.info = rsp.data.info
          })
        }
      }
    },
    checkpassword () {
      if (this.password !== this.password2) {
        this.info2 = '密码不匹配'
      }
    },
    checkusername () {
      if (this.username === '') {
        this.info1 = '不能为空'
      }
    }
  }
}
</script>
<style lang="">
  body{margin: 0; background-color: lightyellow;}
  .formTitle{margin-top: 30px; font-size: 19px;}
  ul{list-style: none;}
  .registerForm{width: 30%; margin: 0 auto; margin-top: 100px; background-color: lightgreen; height: 400px; border-radius: 20px}
  .inputInfo input{width: 60%; height: 30px; font-size: 25px; margin-top: 20px;}
  .registerButton button{width: 50%; height: 30px; display: block; border-radius: 5px; margin: 0 auto; margin-top: 20px;}
  .registerButton button:hover{border: 1px solid blue;}
  span{display: block; height: 10px}
</style>
