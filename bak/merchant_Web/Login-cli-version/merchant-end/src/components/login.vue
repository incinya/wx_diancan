<style>
	.layout {
		height: 100%;
		width: 100%;
	}
	#sign-container {
		position: relative;
    	top: 50%;
		margin: auto;
		width: 400px;
		height: 50%;
		-webkit-transform: translateY(-50%);

	       -moz-transform: translateY(-50%);

	         -ms-transform: translateY(-50%);

	            -o-transform: translateY(-50%);

	                 transform: translateY(-50%);
	}
	#Sign-content {
		height: calc(100% - 52px);
		width: 100%;
		display:inline-block;
		vertical-align: middle;
	}
	#Sign-footer {
		height: 52px;
	}
	.rightbutton {
		font-size: 15px;
		color: #2d8cf0;
		float: right;
		margin-top: 25px;
		cursor:pointer;
	}
	.vertificate-input {
		width: 280px;
	}
	#phone-input, #name-input {
		margin-top: 20px; 
	}
	#password-input {
		margin-top: 25px;
	}
	.ivu-tabs-tabpane {
		padding: 2px;
	}
	.vertificate-input {
		margin-top: 25px; 
		width: 60%;
	}
	#Getvertific-button, #Getvertific-button2{
		margin-top: 25px; 
		width: 30%;
		height: 40px;
		font-size: 18px;
		float: right;
	}
	#Autosign-checkbox {
		margin-top: 25px; 
		font-size: 15px;
	}
	#Sign-footer {
		text-align: center;
	}
	a {
		margin: 5px;
		font-size: 13px;
	}
	.Login-button {
		margin-top: 25px; 
		font-size: 18px;
		height: 50px;
		width: 100%;
	}

	.ivu-input {
		height: 40px;
		font-size: 18px;
	}
	.ivu-tabs-nav {
		width: 100%
	}
	.ivu-tabs-tab {
		width: 50%;
		text-align: center;
		font-size: 20px;
		margin-bottom: 8px;
	}

</style>
<template>
	<div class="layout">
		<div id="Sign-content">
			<div id="sign-container">
				<Tabs value="signup">
					<TabPane label="账户密码登录" name="username">
						<div class="Loginlabel-Name">
							<Input id="name-input" v-model="username" placeholder="用户名"></Input>
							<Input id="password-input" type="password" v-model="password" placeholder="密码"></Input>
							<Input class="vertificate-input" placeholder="验证码"></Input>
							<div id="Getvertific-button2">验证码</div>
							<Checkbox size="large" id="Autosign-checkbox">自动登录</Checkbox>
							<p id="forget-button1" type="text" class="rightbutton">忘记密码</p>
							<Button type="primary" class="Login-button" @click="handleSubmit()">登录</Button>
							<p id="Sign-button" type="text" class="rightbutton">注册账户</p>
						</div>
					</TabPane>
					
					<TabPane label="手机号登录" name="userphone">
						<div class="Signlabel-Phone">
							<Input id="phone-input" placeholder="手机号"></Input>
							<Input class="vertificate-input" placeholder="验证码"></Input>
							<Button id="Getvertific-button">获取验证码</Button>
							<Checkbox size="large" id="Autosign-checkbox">自动登录</Checkbox>
							<p id="forget-button2" type="text" class="rightbutton">忘记密码</p>
							<Button type="primary" class="Login-button">登录</Button>
							<p id="Sign-button" type="text" class="rightbutton">注册账户</p>
						</div>
					</TabPane>
					
				</Tabs>
			</div>
		</div>
		<div id="Sign-footer">
			<div class="SomeLinks">
				<a href="www.baidu.com">帮助</a>
				<a href="www.baidu.com">隐私</a>
				<a href="www.baidu.com">条款</a>
			</div>
			<div class="Team">
				<a>copyright © ChickenDinner8出品</a>
			</div>
		</div>
	</div>
</template>

<script>
export default {
  data () {
    return {
    	username: 'Llunnn',
    	password: '123456'
    }
  },
  methods: {
    handleSubmit () {
    	// 这样发请求就好了
      this.axios.post('/api/boss/login', {
        username: this.username,
        password: this.password
      })
        .then(res => {
          console.log(res)
        })
        .catch(err => {
          console.log('err: ', err)
        });
    }
  }
}
</script>