package com.accessor;

public class User{	
	private String name;
	private String secondName;

	public void setName(String name){
		this.name = name;
	}

	public String getName(){
		return name;
	}

	public void setSecondName(String secondName){
		this.secondName = secondName;
	}

	public String getSecondName(){
		return secondName;
	}

	User(String name){
		this.name = name;
	}

	User(String name, String secondName){
		this(name);
		this.secondName;
	}
}