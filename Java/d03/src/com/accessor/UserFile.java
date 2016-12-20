package com.accessor;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class UserFile {
    private String fileName;
    AccessLevelRecord accessLevelRecord = new AccessLevelRecord(true, true);
    public List<Objects> accessRights = new ArrayList<Objects>(2);


    public UserFile(String fileName, List<Objects> accessRights) {
        this.fileName = fileName;
        this.accessRights = accessRights;
    }

    @Override
    public String toString() {
        return "UserFile{}";
    }
}