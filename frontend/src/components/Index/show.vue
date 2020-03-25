<template>
  <div id="successList" class="container clear">
    <div class="SuccessTitle">
      <h2>成功案例</h2>
    </div>
    <div id="Sample">
      <ul>
        <li>
          <img v-bind:src="workerPng" title="" alt="" width="230px" height="100px">
          <p>小王在##################################表现特别优秀</p>
          <span>优秀员工姓名: 王大王</span>
          <span>状态: 空闲</span>
        </li>
        <li>
          <img v-bind:src="workerPng" title="" alt="" width="230px" height="100px">
          <p>小王在##################################表现特别优秀</p>
          <span>优秀员工姓名: 王大王</span>
          <span>状态: 空闲</span>
        </li>
        <li>
          <img v-bind:src="workerPng" title="" alt="" width="230px" height="100px">
          <p>小王在##################################表现特别优秀</p>
          <span>优秀员工姓名: 王大王</span>
          <span>状态: 空闲</span>
        </li>
        <li>
          <img v-bind:src="workerPng" title="" alt="" width="230px" height="100px">
          <p>小王在##################################表现特别优秀</p>
          <span>优秀员工姓名: 王大王</span>
          <span>状态: 空闲</span>
        </li>
        <li>
          <img v-bind:src="workerPng" title="" alt="" width="230px" height="100px">
          <p>小王在##################################表现特别优秀</p>
          <span>优秀员工姓名: 王大王</span>
          <span>状态: 空闲</span>
        </li>
        <li>
          <img v-bind:src="workerPng" title="" alt="" width="230px" height="100px">
          <p>小王在##################################表现特别优秀</p>
          <span>优秀员工姓名: 王大王</span>
          <span>状态: 空闲</span>
        </li>
        <li>
          <img v-bind:src="workerPng" title="" alt="" width="230px" height="100px">
          <p>小王在##################################表现特别优秀</p>
          <span>优秀员工姓名: 王大王</span>
          <span>状态: 空闲</span>
        </li>
        <li>
          <a><img v-bind:src="workerPng" title="" alt="" width="230px" height="100px"></a>
          <p>小王在##################################表现特别优秀</p>
          <span><a>优秀员工姓名: 王大王</a></span>
          <span>状态: 空闲</span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'show',
  data () {
    return {
      workerPng: '#'
    }
  },
  created () {
    this.workerPng = require('@' + '/assets/Worker.jpg')
  }
}
</script>
<style lang="">
  .clear:after{content: ''; display: block; clear: both;}
  .container{width: 80%; margin: 0 auto;}
  #successList{position: relative;}
  #successList .SuccessTitle h2{text-align: center; font-size: 25px; color:black; font-weight: bold;}
  #Sample{margin-top: 40px;}
  #Sample ul{margin-left: 60px;}
  #Sample li{float: left; display: block; width: 240px; margin-left: 20px;}
  #Sample p{overflow:hidden;}
</style>
