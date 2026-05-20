package com.keycode.TutorCompanion.model;

import java.time.LocalDateTime;

import com.fasterxml.jackson.annotation.JsonBackReference;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "tutoring_suggestions")
public class TutoringSuggestion {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    // estudiante que solicita
    @JsonBackReference
    @ManyToOne
    @JoinColumn(name = "student_id", nullable = false)
    private User student;

    // tutor sugerido
    @JsonBackReference
    @ManyToOne
    @JoinColumn(name = "tutor_id", nullable = false)
    private User tutor;

    @ManyToOne
    @JoinColumn(name = "subject_id", nullable = false)
    private Subject subject;

    @Column(nullable = false)
    private String topic;

    @Column(columnDefinition = "TEXT")
    private String message;

    @Column(nullable = false)
    private String status = "pending";

    @Column(name = "created_at")
    private LocalDateTime createdAt = LocalDateTime.now();

    public TutoringSuggestion() {
    }

    public TutoringSuggestion(
            Long id,
            User student,
            User tutor,
            Subject subject,
            String topic,
            String message,
            String status,
            LocalDateTime createdAt
    ) {
        this.id = id;
        this.student = student;
        this.tutor = tutor;
        this.subject = subject;
        this.topic = topic;
        this.message = message;
        this.status = status;
        this.createdAt = createdAt;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public User getStudent() {
        return student;
    }

    public void setStudent(User student) {
        this.student = student;
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

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(LocalDateTime createdAt) {
        this.createdAt = createdAt;
    }

}