package com.keycode.TutorCompanion.dto;

public record ReviewRequest(
        Long tutorId,
        Long studentId,
        Integer rating,
        String comment
) {
}
