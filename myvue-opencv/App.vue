<template>
  <div class="camera">
    <video ref="videoElement" autoplay></video>
  </div>
</template>

<script>
export default {
  mounted() {
    this.initCamera();
  },
  methods: {
    initCamera() {
      navigator.mediaDevices.getUserMedia({ video: true })
        .then((stream) => {
          const videoElement = this.$refs.videoElement;
          videoElement.srcObject = stream;
        })
        .catch((error) => {
          console.error('Error accessing camera:', error);
        });
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
.camera video {
  max-width: 100%;
  max-height: 100%;
}
</style>
