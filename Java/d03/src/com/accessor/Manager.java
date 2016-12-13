package com.accessor;

import com.accessor.*;
import java.io.File;
import java.io.IOException;

public class Manager{
	public static void main(String[] args) throws IOException {
		//получаем разделитель пути в текущей операционной системе
		String fileSeparator = System.getProperty("file.separator");

		//создаем абсолютный путь к файлу
		String absoluteFilePath = fileSeparator + "com" + fileSeparator + "accessor" + fileSeparator + "file.txt";

		File f1 = new File(absoluteFilePath);
		f1.createNewFile();
	}
}