package com.accessor;

public class User{	
	private String name;

	public void setName(String name){
		this.name = name;
	}

	public String getName(){
		return name;
	}

	User(String name){
		this.name = name;
	}

	@Override
	public String toString(){
		return "Пользователь: " + name;
	}
}