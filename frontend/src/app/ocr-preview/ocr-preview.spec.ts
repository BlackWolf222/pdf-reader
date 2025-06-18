import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OcrPreview } from './ocr-preview';

describe('OcrPreview', () => {
  let component: OcrPreview;
  let fixture: ComponentFixture<OcrPreview>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [OcrPreview]
    })
    .compileComponents();

    fixture = TestBed.createComponent(OcrPreview);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
