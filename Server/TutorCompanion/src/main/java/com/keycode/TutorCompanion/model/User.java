package com.keycode.TutorCompanion.model;

import java.time.LocalDateTime;
import java.util.List;

import com.fasterxml.jackson.annotation.JsonManagedReference;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.JoinTable;
import jakarta.persistence.ManyToMany;
import jakarta.persistence.OneToMany;
import jakarta.persistence.OneToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "users")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, length = 100)
    private String name;

    @Column(nullable = false, unique = true, length = 150)
    private String email;

    @Column(name = "password_hash", nullable = false)
    private String passwordHash;

    private String pfp;

    @Column(name = "is_becado")
    private Boolean isBecado = false;

    private String state = "active";

    @Column(name = "created_at")
    private LocalDateTime createdAt = LocalDateTime.now();

    @ManyToMany
    @JoinTable(
    name = "user_subjects",
    joinColumns = @JoinColumn(name = "user_id"),
    inverseJoinColumns = @JoinColumn(name = "subject_id")
    )
    private List<Subject> subjects;

    @JsonManagedReference
    @OneToOne(mappedBy = "user")
    private TutorProfile tutorProfile;

    @JsonManagedReference
    @OneToOne(mappedBy = "user")
    private Contact contact;

    @JsonManagedReference
    @OneToMany(mappedBy = "tutor")
    private List<TutorSession> sessions;

    @JsonManagedReference
    @OneToMany(mappedBy = "student")
    private List<SessionStudent> enrolledSessions;

    @JsonManagedReference
    @OneToMany(mappedBy = "tutor")
    private List<Review> receivedReviews;

    @JsonManagedReference
    @OneToMany(mappedBy = "student")
    private List<Review> writtenReviews;

    public User() {
    }

    public User(Long id, String name, String email, String passwordHash, String pfp,
            Boolean isBecado, String state, LocalDateTime createdAt) {
        this.id = id;
        this.name = name;
        this.email = email;
        this.passwordHash = passwordHash;
        this.pfp = pfp;
        this.isBecado = isBecado;
        this.state = state;
        this.createdAt = createdAt;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPasswordHash() {
        return passwordHash;
    }

    public void setPasswordHash(String passwordHash) {
        this.passwordHash = passwordHash;
    }

    public String getPfp() {
        return pfp;
    }

    public void setPfp(String pfp) {
        this.pfp = pfp;
    }

    public Boolean getIsBecado() {
        return isBecado;
    }

    public void setIsBecado(Boolean isBecado) {
        this.isBecado = isBecado;
    }

    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(LocalDateTime createdAt) {
        this.createdAt = createdAt;
    }

    public List<Subject> getSubjects() {
        return subjects;
    }

    public void setSubjects(List<Subject> subjects) {
        this.subjects = subjects;
    }

    public TutorProfile getTutorProfile() {
        return tutorProfile;
    }

    public void setTutorProfile(TutorProfile tutorProfile) {
        this.tutorProfile = tutorProfile;
    }

    public Contact getContact() {
        return contact;
    }

    public void setContact(Contact contact) {
        this.contact = contact;
    }

    public List<TutorSession> getSessions() {
        return sessions;
    }

    public void setSessions(List<TutorSession> sessions) {
        this.sessions = sessions;
    }

    public List<SessionStudent> getEnrolledSessions() {
        return enrolledSessions;
    }

    public void setEnrolledSessions(List<SessionStudent> enrolledSessions) {
        this.enrolledSessions = enrolledSessions;
    }

    public List<Review> getReceivedReviews() {
        return receivedReviews;
    }

    public void setReceivedReviews(List<Review> receivedReviews) {
        this.receivedReviews = receivedReviews;
    }

    public List<Review> getWrittenReviews() {
        return writtenReviews;
    }

    public void setWrittenReviews(List<Review> writtenReviews) {
        this.writtenReviews = writtenReviews;
    }

}