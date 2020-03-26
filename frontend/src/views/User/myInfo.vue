<template>
  <div>
    <top></top>
    <div class="MainView">
      <leftBar></leftBar>
      <div class="UserBaseInfo r">
      <div class="clear">
        <h1 class="l">完善程度:</h1>
        <div id="progress"></div>
        <!-- <progress class="l" max="10" value="2" id="progress" style="width: 70%; margin-top: 6px; margin-left: 2%;"></progress> -->
      </div>
      <div><h1 style="text-align: center;">基本信息</h1></div>
      <table border="1" style="border-collapse:collapse;">
        <tr>
          <td colspan="8">您的资料</td>
        </tr>
        <tr>
          <td class="serverInfo">姓名</td>
          <td class="userData">{{userName}}</td>
          <td class="serverInfo">性别</td>
          <td class="userData">
                {{sex}}
          </td>
          <td class="serverInfo">年龄</td>
          <td class="userData">
            {{age}}
          </td>
          <td class="userData" colspan="2" rowspan="2">
          <img v-bind:src="userPhoto" alt="投降" width="60px" height="100px">
          </td>
        </tr>
        <tr>
          <td class="serverInfo">出生日期</td>
          <td class="userData">{{bornDate}}</td>
          <td class="serverInfo">系统角色</td>
          <td class="userData">{{userlevel}}</td>
          <td class="serverInfo">手机号</td>
          <td class="userData">{{telephone}}</td>
        </tr>
        <tr>
          <td class="serverInfo">身份证</td>
          <td class="userData">{{idCard}}</td>
          <td class="serverInfo">现在住址</td>
          <td colspan="2" class="userData">{{address}}</td>
          <td class="serverInfo">籍贯</td>
          <td colspan="2" class="userData">{{oldHome}}</td>
        </tr>
        <tr>
          <td class="serverInfo">邮箱</td>
          <td class="userData">{{email}}</td>
          <td class="serverInfo">紧急联系人</td>
          <td colspan="2" class="userData">{{urgencyUser}}</td>
          <td class="serverInfo">紧急联系人方式</td>
          <td colspan="2" class="userData">{{urgencyContact}}</td>
        </tr>
      </table>
      <div class="editButton">
          <div v-if="isActive">
            <a href="">修改信息</a>
          </div>
          <div v-else>
            <a href="">去激活</a>
          </div>
      </div>
    </div>
    </div>
  </div>
</template>

<script>
import top from '@/components/JiaZheng/top.vue'
import leftBar from '@/components/User/leftBar.vue'
import router from './../../router'
export default {
  name: 'myinfo',
  data () {
    return {
      msg: '#',
      currentAccount: '#',
      localAccount: '#',
      username: '',
      sex: '',
      age: '',
      userPhoto: '',
      bornDate: '',
      userlevel: '',
      telephone: '',
      idCard: '',
      address: '',
      oldHome: '',
      email: '',
      urgencyUser: '',
      urgencyContact: '',
      isActive: false
    }
  },
  components: {
    top,
    leftBar
  },
  created () {
    this.currentAccount = router.history.current.params.id
    this.localAccount = JSON.parse(localStorage.getItem('user')).account
  },
  watch: {
    currentAccount: function (curID) {
      if (curID !== this.localAccount) {
        // router.push({path: '/'})
      }
    }
  }
}
</script>
<style lang="">
  .MainView{position: relative; background-color: blanchedalmond; height: 980px; width: 100%}
  .MainView .leftSideBar{position:absolute; left: 30px; width: 15.6%; height: 600px; border-right:1px solid gray; background-color: lightskyblue;}
  .MainView .leftSideBar li{margin-top: 30px; width: 100; height: 40px; text-align: center;}
  .MainView .leftSideBar a{text-align: center; display: block; width: 100%; height: 100%;
            background-color: lightseagreen; line-height: 40px;}
  .UserBaseInfo{width: 80%; clear: left}
  .UserBaseInfo table{margin: 10px auto; width: 90%; text-align: center; font-size: 18px}
  .UserBaseInfo table{}
  .UserBaseInfo .serverInfo{background-color: cornsilk;}
  .UserBaseInfo .userData{min-width: 80px;}
  .UserBaseInfo .editButton{margin: 0 auto; width: 15%; height: 30px;background-color: aqua;
      border-radius: 5px; text-align: center; line-height: 30px;}
  .UserBaseInfo .editButton a{display: block; width: 100%; height: 100%; color: black;}
  .UserBaseInfo .editButton a:hover{border: 1px solid blue; border-radius: 5px;}
</style>
