<template>
  <div class="leftSideBar">
    <ul>
        <li>
            <a v-bind:href="myinfoRoute">我的资料</a>
        </li>
        <li>
            <a v-bind:href="userSecRoute">账号安全</a>
        </li>
        <li>
            <a href="#">我的服务</a>
        </li>
        <li>
            <a href="#">资金往来</a>
        </li>
        <li>
            <a href="#">其他问题</a>
        </li>
        <router-view></router-view>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'leftBar',
  data () {
    return {
      myinfoRoute: '#',
      userSecRoute: '#'
    }
  },
  created () {
    this.myinfoRoute = '/#/user'
    this.userSecRoute = '/#/user' + '/security'
  }
}
</script>
<style lang="">

</style>
