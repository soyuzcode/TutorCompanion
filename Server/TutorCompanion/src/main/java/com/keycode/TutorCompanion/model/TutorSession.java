package com.keycode.TutorCompanion.model;

import java.time.LocalDateTime;
import java.util.List;

import com.fasterxml.jackson.annotation.JsonBackReference;
import com.fasterxml.jackson.annotation.JsonManagedReference;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.OneToMany;
import jakarta.persistence.Table;

@Entity
@Table(name = "sessions")
public class TutorSession {

    @Id
    private Long id;

    @ManyToOne
    @JoinColumn(name = "tutor_id")
    @JsonBackReference
    private User tutor;

    @ManyToOne
    @JoinColumn(name = "subject_id")
    @JsonBackReference
    private Subject subject;

    private String topic;

    @Column(name = "start_time")
    private LocalDateTime startTime;

    @Column(name = "end_time")
    private LocalDateTime endTime;

    @Column(name = "tutor_status")
    private String tutorStatus;

    private String description;

    @JsonManagedReference
    @OneToMany(mappedBy = "session")
    private List<SessionStudent> students;

    public TutorSession() {
    }

    public TutorSession(Long id, User tutor, Subject subject,
            String topic, LocalDateTime startTime,
            LocalDateTime endTime,
            String tutorStatus,
            String description) {

        this.id = id;
        this.tutor = tutor;
        this.subject = subject;
        this.topic = topic;
        this.startTime = startTime;
        this.endTime = endTime;
        this.tutorStatus = tutorStatus;
        this.description = description;
    }

    public Long getId() {
        return id;
    }

    public User getTutor() {
        return tutor;
    }

    public void setTutor(User tutor) {
        this.tutor = tutor;
    }

    public Subject getSubject() {
        return subject;
    }

    public void setSubject(Subject subject) {
        this.subject = subject;
    }

    public String getTopic() {
        return topic;
    }

    public void setTopic(String topic) {
        this.topic = topic;
    }

    public LocalDateTime getStartTime() {
        return startTime;
    }

    public void setStartTime(LocalDateTime startTime) {
        this.startTime = startTime;
    }

    public LocalDateTime getEndTime() {
        return endTime;
    }

    public void setEndTime(LocalDateTime endTime) {
        this.endTime = endTime;
    }

    public String getTutorStatus() {
        return tutorStatus;
    }

    public void setTutorStatus(String tutorStatus) {
        this.tutorStatus = tutorStatus;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<SessionStudent> getStudents() {
        return students;
    }

    public void setStudents(List<SessionStudent> students) {
        this.students = students;
    }
}