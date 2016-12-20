package com.accessor;

public class AccessLevelRecord {
    private boolean isWritable;
    private boolean isReadable;

    public AccessLevelRecord(boolean isWritable, boolean isReadable) {
        this.isWritable = isWritable;
        this.isReadable = isReadable;
    }

    public void isWritable(boolean writable) {
        isWritable = writable;
    }

    public void isReadable(boolean readable) {
        isReadable = readable;
    }


    @Override
    public String toString() {
        return "AccessLevelRecord{" +
                "isWritable= " + isWritable +
                ", isReadable= " + isReadable +
                '}';
    }
}