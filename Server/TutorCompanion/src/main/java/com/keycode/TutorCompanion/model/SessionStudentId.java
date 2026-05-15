package com.keycode.TutorCompanion.model;

import java.io.Serializable;
import java.util.Objects;

public class SessionStudentId implements Serializable {

    private Long session;
    private Long student;

    public SessionStudentId() {
    }

    public SessionStudentId(Long session, Long student) {
        this.session = session;
        this.student = student;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;

        if (!(o instanceof SessionStudentId))
            return false;

        SessionStudentId that = (SessionStudentId) o;

        return Objects.equals(session, that.session)
                && Objects.equals(student, that.student);
    }

    @Override
    public int hashCode() {
        return Objects.hash(session, student);
    }
}