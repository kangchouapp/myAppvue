<template>
  <div class="camera">
    <img :src="videoSource" alt="Camera Feed">
  </div>
</template>

<script>
export default {
  data() {
    return {
      videoSource: '',
    };
  },
  mounted() {
    this.initCamera();
  },
  methods: {
    initCamera() {
      this.videoSource = 'http://localhost:5000/video_feed';  // 更新视频源为服务器地址
    },
  },
};
</script>

<style scoped>
.camera {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f0f0f0;
}
.camera img {
  max-width: 100%;
  max-height: 100%;
}
</style>
