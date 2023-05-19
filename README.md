# myApp
CV and NLP (vue,python,flask,java,web,c++)


# 项目1：VUE 与 flask 前端交互
![image](https://github.com/KangChou/myApp/assets/36963108/69033173-bf7d-4da9-bc31-9c6ff050f1a0)



# 环境配置

```
在myvue目录下运行Vue项目：







运行npm install可以安装package.json之中的依赖
（这将根据package.json文件中的依赖项列表，自动下载和安装所需的包到node_modules目录中。）
在终端或命令提示符中，运行以下命令全局安装Vue CLI：
npm install -g @vue/cli
python server.py
npm run serve


在项目根目录下执行以下命令，清除旧的构建缓存并重新安装依赖:
$ npm cache clean --force
$ rm -rf node_modules
$ npm install




{
  "name": "myvue", // 项目名称
  "version": "1.0.0", // 项目版本号
  "description": "My Vue project", // 项目描述
  "scripts": {
    "serve": "vue-cli-service serve", // 运行开发服务器的命令
    "build": "vue-cli-service build" // 构建生产版本的命令
  },
  "dependencies": {
    "vue": "^2.6.14" // 项目所依赖的Vue版本
  },
  "devDependencies": {
    // 开发环境所依赖的包
  },
  "author": "Your Name", // 作者名称
  "license": "MIT" // 许可证类型
}




{
  "name": "myvue",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "serve": "vue-cli-service serve"
  },
  "dependencies": {
    "vue": "^2.6.14"
  },
  "devDependencies": {
    "@vue/cli-service": "^4.5.14",
    "@vue/compiler-sfc": "^2.6.14"
  }
  
}

```
