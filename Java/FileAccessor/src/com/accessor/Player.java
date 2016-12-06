package com.accessor;

import java.text.DecimalFormat;

/**
 * Created by Viacheslav on 06.12.2016.
 */
public class Player {
    private String name;
    private double average;

    public Player(String name, double average){
        this.name = name;
        this.average = average;
    }

    public String getName(){
        return name;
    }

    public double getAverage(){
        return average;
    }

    public String getAverageString() {
        DecimalFormat decFormat = new DecimalFormat();
        decFormat.setMaximumIntegerDigits(0);
        decFormat.setMaximumFractionDigits(3);
        decFormat.setMinimumFractionDigits(3);
        return decFormat.format(average);
    }
}
