<template>
	<div class="Loginlabel-Name">
		<Input id="name-input" placeholder="用户名"></Input>
		<Input id="password-input" placeholder="密码"></Input>
		<Input class="vertificate-input" placeholder="验证码"></Input>
		<div id="Getvertific-button2">验证码</div>
		<Checkbox size="large" id="Autosign-checkbox">自动登录</Checkbox>
		<p id="forget-button1" type="text" class="rightbutton">忘记密码</p>
		<Button type="primary" class="Login-button">登录</Button>
		<p id="Sign-button" type="text" class="rightbutton">注册账户</p>
	</div>
</template>
<style scoped>
	.Loginlabel-Name {
		width: 100%;
		height: 100%;
	}
</style>