package com.keycode.TutorCompanion.model;

import com.fasterxml.jackson.annotation.JsonBackReference;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.IdClass;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@IdClass(SessionStudentId.class)
@Table(name = "session_students")
public class SessionStudent {

    @Id
    @ManyToOne
    @JoinColumn(name = "session_id")
    @JsonBackReference
    private TutorSession session;

    @Id
    @ManyToOne
    @JoinColumn(name = "student_id")
    @JsonBackReference
    private User student;

    @Column(name = "student_status")
    private String studentStatus;

    public SessionStudent() {
    }

    public SessionStudent(TutorSession session,
            User student,
            String studentStatus) {

        this.session = session;
        this.student = student;
        this.studentStatus = studentStatus;
    }

    public TutorSession getSession() {
        return session;
    }

    public void setSession(TutorSession session) {
        this.session = session;
    }

    public User getStudent() {
        return student;
    }

    public void setStudent(User student) {
        this.student = student;
    }

    public String getStudentStatus() {
        return studentStatus;
    }

    public void setStudentStatus(String studentStatus) {
        this.studentStatus = studentStatus;
    }
}