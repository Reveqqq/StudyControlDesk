<script>

export default {
  name: 'FooterComp'
}
</script>

<template>
  <footer>
    <div class="footer_left">
      <div class="footer_logo">
        <img src="../../public/images/logo.png" alt="">
      </div>
    </div>
    <div class="footer_right">
      <div class="footer_dir"></div>
    </div>
  </footer>
</template>

<style scoped>
footer{
  display: flex;
  width: 100%;
  height: 100%;
  background: #EFEFEF;
  padding: 20px 200px;
}

footer .footer_left{
  display: flex;
  justify-content: left;
  align-items: center;
  width: 100%;
}

footer .footer_left .footer_logo{
  position: relative;
  width: 320px;
  height: 320px;
  background-size: 100%;
  background: #EFEFEF url("../../public/images/logo_bg.gif") no-repeat 50% 50%;
  background-blend-mode: multiply;
}

footer .footer_left .footer_logo img{
  width: 210px;
  height: 340px;
  position: absolute;
  top: -10px;
  left: 50px;
  object-fit: cover;
}


footer .footer_right{
  display: flex;
  justify-content: left;
  align-items: center;
  width: 100%;
}

footer .footer_right .footer_dir{
  width: 600px;
  height: 250px;
  background: url("../../public/images/dir.gif"), #EFEFEF 50%;
  background-size: 100%;
  background-blend-mode: multiply;
}
</style>