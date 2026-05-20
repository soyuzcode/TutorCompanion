package com.keycode.TutorCompanion.dto;

import com.keycode.TutorCompanion.model.TutoringSuggestion;

public record SuggestionResponse(
        Long id,
        Long studentId,
        String studentName,
        String studentPfp,
        String topic,
        String message,
        String status,
        String createdAt,
        Long subjectId,
        String subjectName
) {
    public static SuggestionResponse from(TutoringSuggestion suggestion) {
        return new SuggestionResponse(
                suggestion.getId(),
                suggestion.getStudent().getId(),
                suggestion.getStudent().getName(),
                suggestion.getStudent().getPfp(),
                suggestion.getTopic(),
                suggestion.getMessage(),
                suggestion.getStatus(),
                suggestion.getCreatedAt() != null
                        ? suggestion.getCreatedAt().toString()
                        : null,
                suggestion.getSubject().getId(),
                suggestion.getSubject().getName());
    }
}
